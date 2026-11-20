import unittest
from unittest.mock import Mock, patch

import requests
from bs4 import BeautifulSoup

from main import fetch_author, fetch_page, parse_author, parse_publications


SCHOLAR_ID = "9VhMC1QAAAAJ"
PROFILE = """
<div id="gsc_prf_in">Xuyang Liu</div>
<table id="gsc_rsb_st"><tbody>
<tr><td>Citations</td><td class="gsc_rsb_std">1,136</td><td class="gsc_rsb_std">1,132</td></tr>
<tr><td>h-index</td><td class="gsc_rsb_std">19</td><td class="gsc_rsb_std">19</td></tr>
<tr><td>i10-index</td><td class="gsc_rsb_std">23</td><td class="gsc_rsb_std">23</td></tr>
</tbody></table>
<span class="gsc_g_t">2026</span><span class="gsc_g_al">830</span>
<table>
<tr class="gsc_a_tr"><td class="gsc_a_t">
<a class="gsc_a_at" href="/citations?citation_for_view=9VhMC1QAAAAJ:paper">Example paper</a>
<div class="gs_gray">X Liu, A Author</div><div class="gs_gray">Example venue, 2026</div>
</td><td class="gsc_a_c"><a class="gsc_a_ac" href="/scholar?cites=123,456">12</a></td>
<td class="gsc_a_y">2026</td></tr>
</table><button id="gsc_bpf_more" disabled>Show more</button>
"""


class CitationParserTests(unittest.TestCase):
    def setUp(self):
        self.page = BeautifulSoup(PROFILE, "html.parser")

    def test_author_total_is_not_sum_of_publication_rows(self):
        author = parse_author(self.page, SCHOLAR_ID)
        self.assertEqual(author["citedby"], 1136)
        self.assertEqual(author["citedby5y"], 1132)
        self.assertEqual(author["cites_per_year"], {"2026": 830})

    def test_publication_ids_and_empty_citations(self):
        paper_id = SCHOLAR_ID + ":paper"
        publications = parse_publications(self.page, SCHOLAR_ID)
        self.assertEqual(publications[paper_id]["num_citations"], 12)
        self.assertEqual(publications[paper_id]["cites_id"], ["123", "456"])
        self.page.select_one(".gsc_a_ac").string = ""
        self.assertEqual(parse_publications(self.page, SCHOLAR_ID)[paper_id]["num_citations"], 0)

    def test_preserves_existing_badge_aliases(self):
        title = "Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models"
        self.page.select_one(".gsc_a_at").string = title
        self.assertIn(SCHOLAR_ID + ":CHSYGLWDkRkC", parse_publications(self.page, SCHOLAR_ID))

    def test_rejects_wrong_profile_and_missing_metrics(self):
        with self.assertRaises(ValueError):
            parse_publications(self.page, "other-profile")
        self.page.select_one(".gsc_rsb_std").decompose()
        with self.assertRaises(ValueError):
            parse_author(self.page, SCHOLAR_ID)

    @patch("main.time.sleep")
    def test_block_page_and_timeouts_have_bounded_retries(self, sleep):
        session = Mock()
        session.get.return_value.text = "<html>Unusual traffic</html>"
        with self.assertRaisesRegex(RuntimeError, "public author profile"):
            fetch_page(session, SCHOLAR_ID, 0)
        self.assertEqual(session.get.call_count, 3)
        self.assertEqual(session.get.call_args.kwargs["timeout"], (10, 30))
        session.reset_mock()
        session.get.side_effect = requests.Timeout("request timed out")
        with self.assertRaisesRegex(RuntimeError, "request timed out"):
            fetch_page(session, SCHOLAR_ID, 0)
        self.assertEqual(session.get.call_count, 3)

    @patch("main.PAGE_SIZE", 1)
    @patch("main.fetch_page")
    def test_paginates_without_losing_publications(self, fetch):
        self.page.select_one("#gsc_bpf_more").attrs.pop("disabled")
        second = BeautifulSoup(PROFILE.replace(":paper", ":second"), "html.parser")
        fetch.side_effect = [self.page, second]
        author = fetch_author(SCHOLAR_ID)
        self.assertEqual(len(author["publications"]), 2)
        self.assertEqual(fetch.call_args.args[2], 1)

    @patch("main.PAGE_SIZE", 1)
    @patch("main.fetch_page")
    def test_rejects_repeated_pagination_results(self, fetch):
        self.page.select_one("#gsc_bpf_more").attrs.pop("disabled")
        fetch.return_value = self.page
        with self.assertRaisesRegex(ValueError, "repeated publication"):
            fetch_author(SCHOLAR_ID)
        self.assertEqual(fetch.call_count, 2)


if __name__ == "__main__":
    unittest.main()
