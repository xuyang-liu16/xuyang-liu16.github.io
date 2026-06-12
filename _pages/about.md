---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
  .page__content .home-intro {
    display: block !important;
    margin: 0.2rem 0 1.35rem !important;
    padding: 1.05rem 1.15rem !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 8px !important;
    background: #ffffff !important;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.04) !important;
  }

  .page__content .home-intro p {
    font-size: 1.03rem !important;
    line-height: 1.72 !important;
  }

  .home-intro p:last-child,
  .home-section-lead p,
  .home-news-timeline .news-content p {
    margin-bottom: 0;
  }

  .page__content .home-section-lead {
    margin: 1.05rem 0 0.78rem !important;
    color: #1f2937 !important;
    font-weight: 700 !important;
  }

  .page__content .research-grid {
    display: grid !important;
    grid-template-columns: repeat(2, minmax(260px, 1fr)) !important;
    gap: 0.85rem !important;
    margin: 0.7rem 0 1.35rem !important;
  }

  .page__content .research-card {
    display: block !important;
    min-height: 100% !important;
    padding: 0.95rem 1rem 1rem !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 8px !important;
    background: #ffffff !important;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.035) !important;
  }

  .page__content .research-card h3 {
    margin: 0 0 0.45rem !important;
    color: #2f3437 !important;
    font-size: 1.04rem !important;
    line-height: 1.25 !important;
  }

  .page__content .research-card p {
    margin-bottom: 0 !important;
    color: #333333 !important;
    font-size: 0.95rem !important;
    line-height: 1.58 !important;
  }

  .page__content .home-news-timeline {
    display: block !important;
    max-height: 340px !important;
    overflow-y: auto !important;
    margin: 0.55rem 0 1.65rem !important;
    padding: 0.85rem 0.95rem 0.2rem 1.35rem !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 8px !important;
    background: #ffffff !important;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.04) !important;
    scrollbar-gutter: stable !important;
  }

  .home-news-timeline ul {
    margin-left: 0;
    padding-left: 0;
    list-style: none;
    margin-bottom: 0;
  }

  .page__content .home-news-timeline li {
    position: relative !important;
    display: grid !important;
    grid-template-columns: 5.85rem minmax(0, 1fr) !important;
    gap: 0.45rem !important;
    margin: 0 0 0.78rem !important;
    padding-left: 1.2rem !important;
    color: #333333 !important;
    line-height: 1.5 !important;
  }

  .home-news-timeline li:after {
    content: "";
    position: absolute;
    left: -0.08rem;
    top: 1rem;
    bottom: -0.95rem;
    width: 2px;
    background: linear-gradient(180deg, rgba(47, 128, 237, 0.88) 0%, rgba(47, 128, 237, 0.42) 32%, rgba(47, 128, 237, 0.08) 68%, rgba(255, 255, 255, 0) 100%);
  }

  .home-news-timeline li:last-child:after {
    display: none;
  }

  .home-news-timeline li:before {
    content: "";
    position: absolute;
    left: -0.32rem;
    top: 0.42rem;
    width: 0.58rem;
    height: 0.58rem;
    border: 2px solid #2f80ed;
    border-radius: 50%;
    background: #ffffff;
    z-index: 1;
  }

  .page__content .home-news-timeline .news-date {
    color: #4b5563 !important;
    font-weight: 800 !important;
    white-space: nowrap !important;
  }

  .page__content .paper-box {
    border: 1px solid #e5e7eb !important;
    border-radius: 8px !important;
    padding: 1.1em !important;
    margin: 1.1em 0 !important;
    background: #ffffff !important;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.04) !important;
  }

  .paper-box .paper-box-image img {
    border-radius: 6px;
    box-shadow: 0 5px 14px rgba(0, 0, 0, 0.16);
  }

  .pub-highlight {
    padding: 0;
    border: 0;
    background: transparent;
  }

  .pub-section-heading {
    margin-top: 1.35rem;
    padding-bottom: 0.35rem;
    border-bottom: 1px solid #e5e7eb;
    color: #2f3437;
  }

  .page__content .structured-grid {
    display: grid !important;
    grid-template-columns: repeat(2, minmax(260px, 1fr)) !important;
    gap: 0.85rem !important;
    margin: 0.8rem 0 1.35rem !important;
  }

  .page__content .structured-card {
    border: 1px solid #e5e7eb !important;
    border-radius: 8px !important;
    padding: 0.9rem 1rem !important;
    background: #ffffff !important;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.035) !important;
  }

  .page__content .structured-card h3 {
    margin: 0 0 0.42rem !important;
    color: #2f3437 !important;
    font-size: 1rem !important;
    line-height: 1.28 !important;
  }

  .page__content .structured-card p,
  .page__content .structured-card ul {
    margin-bottom: 0 !important;
  }

  .page__content .structured-card ul {
    padding-left: 1.05rem !important;
  }

  .page__content .structured-card li {
    margin-bottom: 0.2rem !important;
  }

  .page__content .timeline-card {
    display: grid !important;
    grid-template-columns: 11rem minmax(0, 1fr) !important;
    gap: 0.85rem !important;
    align-items: start !important;
  }

  .page__content .timeline-date {
    color: #4b5563 !important;
    font-weight: 800 !important;
    white-space: nowrap !important;
  }

  .page__content .timeline-list {
    display: grid !important;
    grid-template-columns: 1fr !important;
    gap: 0.7rem !important;
    margin: 0.8rem 0 1.35rem !important;
    position: relative !important;
    padding-left: 1.35rem !important;
  }

  .page__content .timeline-list .timeline-card {
    position: relative !important;
  }

  .page__content .timeline-list .timeline-card:before {
    content: "";
    position: absolute;
    left: -1.72rem;
    top: 1.08rem;
    width: 0.62rem;
    height: 0.62rem;
    border: 2px solid #2f80ed;
    border-radius: 50%;
    background: #ffffff;
    z-index: 1;
  }

  .page__content .timeline-list .timeline-card:after {
    content: "";
    position: absolute;
    left: -1.43rem;
    top: 1.68rem;
    bottom: -0.95rem;
    width: 2px;
    background: linear-gradient(180deg, rgba(47, 128, 237, 0.88) 0%, rgba(47, 128, 237, 0.42) 32%, rgba(47, 128, 237, 0.08) 68%, rgba(255, 255, 255, 0) 100%);
  }

  .page__content .timeline-list .timeline-card:last-child:after {
    display: none;
  }

  .page__content .service-list {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 0.42rem !important;
    margin: 0.35rem 0 0 !important;
    padding-left: 0 !important;
    list-style: none !important;
  }

  .page__content .service-list li {
    margin: 0 !important;
    padding: 0.2rem 0.5rem !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 999px !important;
    background: #ffffff !important;
    font-size: 0.92rem !important;
  }

  @media (max-width: 37.5em) {
    .page__content .research-grid,
    .page__content .home-news-timeline li,
    .page__content .structured-grid,
    .page__content .timeline-card {
      grid-template-columns: 1fr !important;
    }
  }
</style>

<div class="home-intro" markdown="1">

🌈 I am Xuyang Liu (刘旭洋), an incoming PhD student at [PolyU](https://www.polyu.edu.hk/) <a href='https://www.polyu.edu.hk/' target="_blank"><img src='./images/polyu_logo.png' align="center" style='vertical-align: middle; width: 21px;'></a>, where I will join the [VC Lab](https://polyu-vclab.github.io/) <a href='https://polyu-vclab.github.io/' target="_blank"><img src='./images/vclab_logo.png.jpg' align="center" style='vertical-align: middle; width: 22px;'></a> under the supervision of Prof. [Lei Zhang](https://www4.comp.polyu.edu.hk/~cslzhang/) (IEEE Fellow). I am also currently working as a research intern at [OPPO Research Institute](https://www.oppo.com/uk/) <a href='https://www.oppo.com/uk/' target="_blank"><img src='./images/oppo_logo.png' align="center" style='vertical-align: middle; width: 52px;'></a>. Previously, I earned my M.S. from [Sichuan University](https://en.scu.edu.cn/) <a href='https://en.scu.edu.cn/' target="_blank"><img src='./images/scu_logo.png' align="center" style='vertical-align: middle; width: 22px;'></a> and spent a wonderful year interning at [Taobao & Tmall Group](https://talent.taotian.com/) <a href='https://talent.taotian.com/' target="_blank"><img src='./images/taobao_logo.png' align="center" style='vertical-align: middle; width: 22px;'></a> and [Ant Group](https://www.antgroup.com/en) <a href='https://www.antgroup.com/en' target="_blank"><img src='./images/alipay_logo.png' align="center" style='vertical-align: middle; width: 22px;'></a>. I am fortunate to work closely with Dr. [Siteng Huang](https://kyonhuang.top/) and Prof. [Linfeng Zhang](http://www.zhanglinfeng.tech/).

</div>

<div class="home-section-lead" markdown="1">

📌 My research centers on **Efficient Multimodal Large Language Models (MLLMs)**, including:

</div>

<div class="research-grid" markdown="1">
<div class="research-card" markdown="1">

### 🖼️ Image Understanding
High-resolution understanding via context compression and fast decoding, including [GlobalCom<sup>2</sup>](https://arxiv.org/abs/2501.05179)<sub>[AAAI'26]</sub>, [V<sup>2</sup>Drop](https://arxiv.org/abs/2509.01552)<sub>[CVPR'26]</sub>, [FiCoCo](https://arxiv.org/abs/2411.17686)<sub>[AAAI'26]</sub>, and [MixKV](https://arxiv.org/abs/2510.20707)<sub>[ICLR'26]</sub>.

</div>
<div class="research-card" markdown="1">

### 🎬 Video Understanding
Long/audio-video, and streaming reasoning via efficient encoding and compression, including [VidCom<sup>2</sup>](https://arxiv.org/abs/2505.14454)<sub>[EMNLP'25]</sub>, [STC](https://arxiv.org/pdf/2512.00891)<sub>[CVPR'26]</sub>, [V-CAST](https://arxiv.org/abs/2603.27650), and [OmniSIFT](https://arxiv.org/abs/2602.04804)<sub>[ICML'26]</sub>.

</div>
<div class="research-card" markdown="1">

### 🎨 Content Generation
Lightweight and efficient AIGC via feature caching, pruning and fast decoding, including [ToCa](https://arxiv.org/abs/2410.05317)<sub>[ICLR'25]</sub>, [Flash-Unified](https://arxiv.org/abs/2603.15271)<sub>[CVPR'26 Findings]</sub>, and [STDec](https://arxiv.org/abs/2604.06330).

</div>
<div class="research-card" markdown="1">

### ⚙️ Efficiency Toolbox
Efficient transfer/fine-tuning and benchmarking for downstream task adaptation, including [M2IST](https://arxiv.org/abs/2407.01131)<sub>[TCSVT'25]</sub>, [V-PETL](https://openreview.net/forum?id=yS1dUkQFnu)<sub>[NeurIPS'24]</sub> and [AutoGnothi](https://arxiv.org/abs/2410.21815)<sub>[ICLR'25]</sub>.

</div>
</div>

📢 If you find these directions interesting, feel free to reach out via email: `liuxuyang@stu.scu.edu.cn`.

## 🔥 News

<div class="news-scroll home-news-timeline">

<ul>
  <li><span class="news-date">2026.04.30</span><div class="news-content">🎊🎊 One paper <a href="https://arxiv.org/abs/2602.04804">OmniSIFT</a> about modality-asymmetric token compression for efficient OmniLLMs has been accepted by <strong>ICML 2026</strong>! Congratulations to all collaborators!</div></li>
  <li><span class="news-date">2026.03.31</span><div class="news-content">🙌🙌 We release <a href="https://arxiv.org/abs/2603.27650">V-CAST</a>, a <strong>curvature-aware</strong> spatio-temporal pruning framework for efficient long-context video inference. V-CAST achieves new SOTA of VideoLLM acceleration! <a href="https://github.com/xinyouu/V-CAST">Code</a> is available!</div></li>
  <li><span class="news-date">2026.02.21</span><div class="news-content">🎊🎊 Four papers have been accepted by <strong>CVPR 2026</strong>, including token compression for VLMs via <a href="https://arxiv.org/abs/2509.01552">V<sup>2</sup>Drop</a>, efficient streaming video understanding via <a href="https://arxiv.org/abs/2512.00891">STC</a>, and token compression for autonomous driving via <a href="https://arxiv.org/abs/2508.13305">Prune2Drive</a> to the main conference, and <a href="https://arxiv.org/abs/2603.15271">Flash-Unified</a> to the findings!</div></li>
  <li><span class="news-date">2026.01.26</span><div class="news-content">🎊🎊 Two papers have been accepted by <strong>ICLR 2026</strong>, including fast decoding for VLM/LLM via <a href="https://arxiv.org/abs/2510.20707">MixKV</a> and the first safety study of dLLMs <a href="https://arxiv.org/abs/2507.11097">DIJA</a>! Congratulations to all collaborators!</div></li>
  <li><span class="news-date">2025.11.08</span><div class="news-content">🎊🎊 Three papers have been accepted by <strong>AAAI 2026</strong>, including two LVLM acceleration methods <a href="https://arxiv.org/abs/2501.05179">GlobalCom<sup>2</sup></a> and <a href="https://arxiv.org/abs/2411.17686">FiCoCo</a>, and a RL-based GUI grounding training framework <a href="https://arxiv.org/abs/2507.15846">GUI-G<sup>2</sup></a>!</div></li>
  <li><span class="news-date">2025.08.21</span><div class="news-content">🎊🎊 One first author paper <a href="https://arxiv.org/abs/2505.14454">VidCom<sup>2</sup></a> about plug-and-play inference acceleration for VideoLLMs has been accepted by <strong>EMNLP 2025</strong> main conference! <a href="https://github.com/xuyang-liu16/VidCom2">Code</a> is available!</div></li>
  <li><span class="news-date">2025.05.27</span><div class="news-content">🙌🙌 We release a new <a href="https://arxiv.org/abs/2505.19147">paper</a>, pointing to <strong>shifting AI efficiency from model-centric to data-centric compression</strong>. <a href="https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression">Project</a> is available! Our paper is honored to be the <a href="https://huggingface.co/papers/2505.19147">#2 Paper of the day</a>!</div></li>
  <li><span class="news-date">2025.03.11</span><div class="news-content">🎊🎊 One first author paper (<a href="https://arxiv.org/abs/2407.01131">M2IST</a>) about parameter-, memory-, and time-efficient fine-tuning for referring expression comprehension has been accepted by IEEE Transactions on Circuits and Systems for Video Technology (<strong>TCSVT</strong>)!</div></li>
  <li><span class="news-date">2025.02.22</span><div class="news-content">🎊🎊 Two papers (<a href="https://arxiv.org/abs/2410.05317">ToCa</a> and <a href="https://arxiv.org/abs/2410.21815">AutoGnothi</a>) have been accepted by <strong>ICLR 2025</strong>! Congratulations to all collaborators!</div></li>
  <li><span class="news-date">2024.09.26</span><div class="news-content">🎊🎊 One co-first author paper (<a href="https://openreview.net/forum?id=yS1dUkQFnu">V-PETL</a>) about unified visual parameter-efficient transfer learning benchmark has been accepted by <strong>NeurIPS 2024</strong>!</div></li>
</ul>

</div>


## 📝 Publications 

Full publications are on my [Google Scholar](https://scholar.google.com/citations?user=9VhMC1QAAAAJ&hl=en) profile. *: Equal contribution. †: Project leader. <a href="https://scholar.google.com/citations?user=9VhMC1QAAAAJ" target="_blank"><img src="https://img.shields.io/badge/dynamic/json?label=Paper%20Citations&query=total_citations&url=https%3A%2F%2Fcse.bth.se%2F~fer%2Fgooglescholar-api%2Fgooglescholar.php%3Fuser%3D9VhMC1QAAAAJ&logo=googlescholar&style=social" alt="Google Scholar"></a>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/MixKV_teaser.png' alt="MixKV teaser" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models**](https://openreview.net/forum?id=B2iqbCQviR)

<u>Xuyang Liu</u><sup>*</sup>, Xiyan Gui<sup>*</sup>, Yuchao Zhang, Linfeng Zhang

- **Model Capability**: LLaVA, Qwen-VL, InternVL, Llama, Mistral.
- **Seamless Integration**: SnapKV, AdaKV, SparseMM.
- **Strong Performance**: **+5.1%** gain across 5 tasks, no speed/memory cost.

<div style="display: inline">
  <a href="https://arxiv.org/pdf/2510.20707"><strong>[paper]</strong></a>
  <a href="https://github.com/xuyang-liu16/MixKV"><strong>[code]</strong></a>
  <a href="https://xuyang-liu16.github.io/MixKV/"><strong>[page]</strong></a>
  <a href="http://xhslink.com/o/9VKjxY3ZWbW"><strong>[Xiaohongshu]</strong></a>
  <a href="https://mp.weixin.qq.com/s/O1mIsIt6LSTZhAF536vGiA"><strong>[量子位]</strong></a>
</div>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025</div><img src='images/VidCom2_teaser.png' alt="VidCom2 teaser" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models**](https://aclanthology.org/2025.emnlp-main.98/)

<u>Xuyang Liu</u><sup>*</sup>, Yiyu Wang<sup>*</sup>, Junpeng Ma, Linfeng Zhang

- **Model Capability**: LLaVA, Qwen-VL, Qwen-Omni.
- **Token Compression**: Only **25%** tokens, **99.6%** performance.
- **Fast Inference**: **-70.8%** generation time, **-43.0%** latency.

<div style="display: inline">
  <a href="https://arxiv.org/pdf/2505.14454"><strong>[paper]</strong></a>
  <a href="https://github.com/xuyang-liu16/VidCom2"><strong>[code]</strong></a>
  <a href="https://xuyang-liu16.github.io/VidCom2/"><strong>[page]</strong></a>
  <a href="http://xhslink.com/o/7SMiHSgXFFU"><strong>[Xiaohongshu]</strong></a>
  <a href="https://www.jiqizhixin.com/articles/2025-12-15-6"><strong>[机器之心]</strong></a>
  <a href="/files/EMNLP-2025-main-262.pdf"><strong>[slides]</strong></a>
  <a href="/files/EMNLP-2025-main-262-Poster.pdf"><strong>[poster]</strong></a>
</div>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='images/GlobalCom2_teaser.png' alt="GlobalCom2 teaser" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**Global Compression Commander: Plug-and-Play Inference Acceleration for High-Resolution Large Vision-Language Models**](https://arxiv.org/abs/2501.05179)

<u>Xuyang Liu</u>, Ziming Wang, Junjie Chen, Yuhang Han, Yingyao Wang, Jiale Yuan, Jun Song, Siteng Huang, Honggang Chen

- **Model Capability**: LLaVA-NeXT, LLaVA-OV.
- **Token Compression**: Only **10%** tokens, **90%+** on **10** tasks.
- **High Efficiency**: FLOPs **9.1%**, memory **60%**, **1.8×** throughput.

<div style="display: inline">
  <a href="https://arxiv.org/pdf/2501.05179"><strong>[paper]</strong></a>
  <a href="https://github.com/xuyang-liu16/GlobalCom2"><strong>[code]</strong></a>
  <a href="/files/AAAI-2026-GlobalCom2-Poster.pdf"><strong>[poster]</strong></a>
</div>

</div>
</div>

<style>
  .pub-filters {
    display: flex;
    gap: 0.45rem;
    flex-wrap: wrap;
    margin: 1rem 0 0.4rem;
  }

  .pub-filter-btn {
    appearance: none;
    border: 1px solid #00369f;
    border-radius: 4px;
    background: transparent;
    color: #111111;
    cursor: pointer;
    font-size: 0.8rem;
    font-weight: 600;
    line-height: 1.1;
    padding: 0.24rem 0.58rem;
    transition: background-color 0.2s ease, color 0.2s ease, border-color 0.2s ease;
  }

  .pub-filter-btn:hover,
  .pub-filter-btn.is-active {
    background: #00369f;
    border-color: #00369f;
    color: #ffffff;
  }

  .pub-highlight {
    margin: 0 0 1.15rem;
    color: inherit;
    font-size: 0.95rem;
    font-weight: 600;
  }

  .pub-marker {
    display: none;
  }

  .pub-item.is-hidden,
  .pub-section-heading.is-hidden,
  .pub-section-box.is-hidden {
    display: none;
  }

  .pub-section-box {
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    background: #ffffff;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.035);
    margin: 1rem 0 1.3rem;
    padding: 0.8rem 1rem 0.2rem;
  }

  .pub-section-box .pub-section-heading {
    margin-top: 0;
  }

  .pub-section-box .pub-item {
    border-bottom: 1px solid #eef0f3;
    margin: 0;
    padding: 0.72rem 0;
  }

  .pub-section-box .pub-item:last-child {
    border-bottom: 0;
  }

  .pub-authors,
  .paper-box-text > p:nth-of-type(2) {
    color: #9aa0a6;
  }

  .pub-authors u,
  .pub-authors u + sup,
  .paper-box-text > p:nth-of-type(2) u,
  .paper-box-text > p:nth-of-type(2) u + sup {
    color: #2f3437;
    font-weight: 700;
  }

</style>

<div class="pub-filters" id="pub-filters" aria-label="Publication filters">
  <button type="button" class="pub-filter-btn is-active" data-filter="all">All</button>
  <button type="button" class="pub-filter-btn" data-filter="first-author">Core</button>
  <button type="button" class="pub-filter-btn" data-filter="physical-first">First</button>
</div>

<div class="pub-highlight" id="pub-highlight">🚩 Highlight: ICLR: 4, ICML: 1, NeurIPS: 1, CVPR: 4, AAAI: 3, EMNLP: 1.</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    var filterRoot = document.getElementById("pub-filters");
    if (!filterRoot) return;

    var buttons = Array.prototype.slice.call(filterRoot.querySelectorAll(".pub-filter-btn"));
    var headings = Array.prototype.slice.call(document.querySelectorAll(".pub-section-heading"));
    var sections = headings.map(function (heading) {
      var items = [];
      var current = heading.nextElementSibling;

      while (current) {
        if (current.classList && current.classList.contains("pub-section-heading")) break;
        if (current.tagName === "H2") break;

        if (current.querySelector && current.querySelector(".pub-marker")) {
          current.classList.add("pub-item");
          items.push(current);
        }

        current = current.nextElementSibling;
      }

      return {
        heading: heading,
        items: items
      };
    });

    function enhanceAuthors(item) {
      var marker = item.querySelector(".pub-marker");
      if (!marker || item.querySelector(".pub-authors")) return;

      var authorSpan = document.createElement("span");
      authorSpan.className = "pub-authors";
      var current = marker.nextSibling;

      while (current) {
        var next = current.nextSibling;

        if (current.nodeType === Node.TEXT_NODE) {
          var quoteIndex = current.nodeValue.indexOf("\"");
          if (quoteIndex !== -1) {
            var before = current.nodeValue.slice(0, quoteIndex);
            var after = current.nodeValue.slice(quoteIndex);
            if (before) authorSpan.appendChild(document.createTextNode(before));
            current.nodeValue = after;
            item.insertBefore(authorSpan, current);
            return;
          }
        }

        if (current.nodeType === Node.ELEMENT_NODE && current.tagName === "STRONG") break;
        authorSpan.appendChild(current);
        current = next;
      }

      if (authorSpan.childNodes.length) item.insertBefore(authorSpan, current);
    }

    sections.forEach(function (section) {
      var box = document.createElement("div");
      box.className = "pub-section-box";
      section.heading.parentNode.insertBefore(box, section.heading);
      box.appendChild(section.heading);
      section.items.forEach(function (item) {
        enhanceAuthors(item);
        box.appendChild(item);
      });
      section.box = box;
    });

    function applyFilter(filter) {
      buttons.forEach(function (button) {
        var isActive = button.getAttribute("data-filter") === filter;
        button.classList.toggle("is-active", isActive);
        button.setAttribute("aria-pressed", isActive ? "true" : "false");
      });

      sections.forEach(function (section) {
        var visibleCount = 0;

        section.items.forEach(function (item) {
          var marker = item.querySelector(".pub-marker");
          var isFirstAuthor = marker && marker.getAttribute("data-first-author") === "true";
          var isPhysicalFirst = marker && marker.getAttribute("data-physical-first") === "true";
          var shouldShow = filter === "all" || (filter === "first-author" && isFirstAuthor) || (filter === "physical-first" && isPhysicalFirst);

          item.classList.toggle("is-hidden", !shouldShow);
          if (shouldShow) visibleCount += 1;
        });

        section.heading.classList.toggle("is-hidden", visibleCount === 0);
        if (section.box) section.box.classList.toggle("is-hidden", visibleCount === 0);
      });
    }

    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        applyFilter(button.getAttribute("data-filter"));
      });
    });

    applyFilter("all");
  });
</script>

<h3 class="pub-section-heading">Conference Papers</h3>

<a href="https://arxiv.org/abs/2602.04804" target="_blank"><img src="https://img.shields.io/badge/ICML-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" data-physical-first="false" aria-hidden="true"></span> Yue Ding, Yiyan Ji, Jungang Li, <u>Xuyang Liu</u>, Xinlong Chen, and 10 more authors, &quot;**OmniSIFT: Modality-Asymmetric Token Compression for Efficient Omni-modal Large Language Models**&quot;. In *International Conference on Machine Learning (ICML)*, 2026. [[paper](https://arxiv.org/pdf/2602.04804)] [[code](https://github.com/dingyue772/OmniSIFT)] [[huggingface paper](https://huggingface.co/papers/2602.04804)] [[量子位](https://mp.weixin.qq.com/s/49yUBxtEFqdST85g4ROQZQ)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:rO6llkc54NcC' href="" target="_blank"></a>

<a href="https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Accelerating_Streaming_Video_Large_Language_Models_via_Hierarchical_Token_Compression_CVPR_2026_paper.html" target="_blank"><img src="https://img.shields.io/badge/CVPR-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" data-physical-first="false" aria-hidden="true"></span> Yiyu Wang<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*,†</sup>, Xiyan Gui, Xinying Lin, Boxue Yang, Chenfei Liao, Tailai Chen, Linfeng Zhang, &quot;**Accelerating Streaming Video Large Language Models via Hierarchical Token Compression**&quot;. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2026. [[paper](https://arxiv.org/pdf/2512.00891)] [[code](https://github.com/lern-to-write/STC)] [[Xiaohongshu](http://xhslink.com/o/5Vm008DxkkH 
)] [[PaperWeekly](https://mp.weixin.qq.com/s/PsNkR28yIFXqAQmAb62Yrg
)] <a href="https://github.com/lern-to-write/STC" target="_blank"><img src="https://img.shields.io/github/stars/lern-to-write/STC?style=social"></a>

<a href="https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Variation-aware_Vision_Token_Dropping_for_Faster_Large_Vision-Language_Models_CVPR_2026_paper.html" target="_blank"><img src="https://img.shields.io/badge/CVPR-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" data-physical-first="false" aria-hidden="true"></span> Junjie Chen<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*,†</sup>, Zichen Wen, Yiyu Wang, Siteng Huang, Honggang Chen, &quot;**Variation-aware Vision Token Dropping for Faster Large Vision-Language Models**&quot;. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2026. [[paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_Variation-aware_Vision_Token_Dropping_for_Faster_Large_Vision-Language_Models_CVPR_2026_paper.pdf)] [[code](https://github.com/xuyang-liu16/V2Drop)] [[机器之心](https://mp.weixin.qq.com/s/5dGS58sg29qLA4mKOLS9bQ)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:RYcK_YlVTxYC' href="" target="_blank"></a> <a href="https://github.com/xuyang-liu16/V2Drop" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/V2Drop?style=social"></a>

<a href="https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_Prune2Drive_A_Plug-and-Play_Framework_for_Accelerating_Vision-Language_Models_in_Autonomous_CVPR_2026_paper.html" target="_blank"><img src="https://img.shields.io/badge/CVPR-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" data-physical-first="false" aria-hidden="true"></span> Minhao Xiong, Zichen Wen, Zhuangcheng Gu, <u>Xuyang Liu</u>, Rui Zhang, Hengrui Kang, Jiabing Yang, Junyuan Zhang, Weijia Li, Conghui He, Yafei Wang, Linfeng Zhang, &quot;**Prune2Drive: A Plug-and-Play Framework for Accelerating Vision-Language Models in Autonomous Driving**&quot;. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2026. [[paper](https://arxiv.org/pdf/2508.13305)] [[code](https://github.com/MinhaoXiong/Prune2Drive)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:NaGl4SEjCO4C' href="" target="_blank"></a>

<a href="https://openaccess.thecvf.com/content/CVPR2026F/html/Ke_Flash-Unified_A_Training-Free_and_Task-Aware_Acceleration_Framework_for_Native_Unified_CVPRF_2026_paper.html" target="_blank"><img src="https://img.shields.io/badge/CVPR-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" data-physical-first="false" aria-hidden="true"></span> Junlong Ke, Zichen Wen, Boxue Yang, Yantai Yang, <u>Xuyang Liu</u>, Chenfei Liao, Zhaorun Chen, Shaobo Wang, Linfeng Zhang, &quot;**Flash-Unified: A Training-Free and Task-Aware Acceleration Framework for Native Unified Models**&quot;. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Findings*, 2026. [[paper](https://arxiv.org/pdf/2603.15271)] [[code](https://github.com/Rirayh/FlashU)]

<a href="https://openreview.net/forum?id=B2iqbCQviR" target="_blank"><img src="https://img.shields.io/badge/ICLR-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" data-physical-first="true" aria-hidden="true"></span> <u>Xuyang Liu</u><sup>\*</sup>, Xiyan Gui<sup>\*</sup>, Yuchao Zhang, Linfeng Zhang, &quot;**Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models**&quot;. In *International Conference on Learning Representations (ICLR)*, 2026. [[paper](https://arxiv.org/pdf/2510.20707)] [[code](https://github.com/xuyang-liu16/MixKV)] [[page](https://xuyang-liu16.github.io/MixKV/)] [[Xiaohongshu](http://xhslink.com/o/9VKjxY3ZWbW)] [[量子位](https://mp.weixin.qq.com/s/O1mIsIt6LSTZhAF536vGiA)] <a href="https://github.com/xuyang-liu16/MixKV" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/MixKV?style=social"></a>

<a href="https://openreview.net/forum?id=rIPeatvPy3" target="_blank"><img src="https://img.shields.io/badge/ICLR-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" data-physical-first="false" aria-hidden="true"></span> Zichen Wen, Jiashu Qu, Dongrui Liu, Zhiyuan Liu, Ruixi Wu, Yicun Yang, Xiangqi Jin, Haoyun Xu, <u>Xuyang Liu</u>, Weijia Li, Chaochao Lu, Jing Shao, Conghui He, Linfeng Zhang, &quot;**The Devil behind the mask: An emergent safety vulnerability of Diffusion LLMs**&quot;. In *International Conference on Learning Representations (ICLR)*, 2026. [[paper](https://arxiv.org/pdf/2507.11097)] [[code](https://github.com/ZichenWen1/DIJA)] [[huggingface paper](https://huggingface.co/papers/2507.11097)] [[量子位](https://mp.weixin.qq.com/s/nfyZFXN7ku07_9tTzG-W9Q)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:BqipwSGYUEgC' href="" target="_blank"></a> <a href="https://github.com/ZichenWen1/DIJA" target="_blank"><img src="https://img.shields.io/github/stars/ZichenWen1/DIJA?style=social"></a> 

<a href="https://ojs.aaai.org/index.php/AAAI/article/view/37673" target="_blank"><img src="https://img.shields.io/badge/AAAI-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" data-physical-first="true" aria-hidden="true"></span> <u>Xuyang Liu</u>, Ziming Wang, Junjie Chen, Yuhang Han, Yingyao Wang, Jiale Yuan, Jun Song, Siteng Huang, Honggang Chen, &quot;**Global Compression Commander: Plug-and-Play Inference Acceleration for High-Resolution Large Vision-Language Models**&quot;. In *Proceedings of the 40th AAAI Conference on Artificial Intelligence*, 2026. [[paper](https://arxiv.org/pdf/2501.05179)] [[code](https://github.com/xuyang-liu16/GlobalCom2)] [[poster](/files/AAAI-2026-GlobalCom2-Poster.pdf)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:yD5IFk8b50cC' href="" target="_blank"></a>
 <a href="https://github.com/xuyang-liu16/GlobalCom2" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/GlobalCom2?style=social"></a>

<a href="https://ojs.aaai.org/index.php/AAAI/article/view/42460" target="_blank"><img src="https://img.shields.io/badge/AAAI-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" data-physical-first="false" aria-hidden="true"></span> Yuhang Han<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Zihan Zhang, Pengxiang Ding, Junjie Chen, Donglin Wang, Honggang Chen, Qingsen Yan, Siteng Huang, &quot;**Filter, Correlate, Compress: Training-Free Token Reduction for MLLM Acceleration**&quot;. In *Proceedings of the 40th AAAI Conference on Artificial Intelligence*, 2026. [[paper](https://arxiv.org/pdf/2411.17686)] [[page](https://ficoco-accelerate.github.io/)] [[code](https://github.com/kawhiiiileo/FiCoCo)][[poster](/files/AAAI-2026-Poster-FiCoCo.pdf)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:cFHS6HbyZ2cC' href="" target="_blank"></a> <a href="https://github.com/kawhiiiileo/FiCoCo" target="_blank"><img src="https://img.shields.io/github/stars/kawhiiiileo/FiCoCo?style=social"></a>

<a href="https://ojs.aaai.org/index.php/AAAI/article/view/40606" target="_blank"><img src="https://img.shields.io/badge/AAAI-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" data-physical-first="false" aria-hidden="true"></span> Fei Tang, Zhangxuan Gu, Zhengxi Lu, <u>Xuyang Liu</u>, Shuheng Shen, Changhua Meng, Wen Wang, Wenqi Zhang, Yongliang Shen, Weiming Lu, Jun Xiao, Yueting Zhuang, &quot;**GUI-G<sup>2</sup>: Gaussian Reward Modeling for GUI Grounding**&quot;. In *Proceedings of the 40th AAAI Conference on Artificial Intelligence*, 2026. [[paper](https://arxiv.org/pdf/2507.15846)] [[code](https://github.com/zju-real/GUI-G2)] [[huggingface paper](https://huggingface.co/papers/2507.15846)] [[page](https://zju-real.github.io/GUI-G2)] [[机器之心](https://mp.weixin.qq.com/s/DRMtB-o9X_CzEFGkxw0Ycw)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:ns9cj8rnVeAC' href="" target="_blank"></a> <a href="https://github.com/zju-real/GUI-G2" target="_blank"><img src="https://img.shields.io/github/stars/zju-real/GUI-G2?style=social"></a>

<a href="https://aclanthology.org/2025.emnlp-main.98/" target="_blank"><img src="https://img.shields.io/badge/EMNLP-2025-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" data-physical-first="true" aria-hidden="true"></span> <u>Xuyang Liu</u><sup>\*</sup>, Yiyu Wang<sup>\*</sup>, Junpeng Ma, Linfeng Zhang, &quot;**Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models**&quot;. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2025. [[paper](https://arxiv.org/pdf/2505.14454)] [[code](https://github.com/xuyang-liu16/VidCom2)] [[page](https://xuyang-liu16.github.io/VidCom2/)] [[Xiaohongshu](http://xhslink.com/o/7SMiHSgXFFU)] [[机器之心](https://www.jiqizhixin.com/articles/2025-12-15-6)] [[PaperWeekly](https://mp.weixin.qq.com/s/hQhEPlBWd4noVGSOWT4_XQ)] [[slides](/files/EMNLP-2025-main-262.pdf)] [[poster](/files/EMNLP-2025-main-262-Poster.pdf)] [[video](https://underline.io/events/502/posters/20833/poster/129850-video-compression-commander-plug-and-play-inference-acceleration-for-video-large-language-models)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:a0OBvERweLwC' href="" target="_blank"></a> <a href="https://github.com/xuyang-liu16/VidCom2" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/VidCom2?style=social"></a>

<a href="https://openreview.net/forum?id=yYZbZGo4ei" target="_blank"><img src="https://img.shields.io/badge/ICLR-2025-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" data-physical-first="false" aria-hidden="true"></span> Chang Zou<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Ting Liu, Siteng Huang, Linfeng Zhang, &quot;**Accelerating Diffusion Transformers with Token-wise Feature Caching**&quot;. In *International Conference on Learning Representations (ICLR)*, 2025. [[paper](https://arxiv.org/pdf/2410.05317)] [[page](https://toca2024.github.io/ToCa/)] [[code](https://github.com/Shenyi-Z/ToCa)] [[量子位](https://mp.weixin.qq.com/s/ZqVWslSEdjX00VMf6RqtcA)] [[poster](/files/ICLR-2025-ToCa-Poster.pdf)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:TQgYirikUcIC' href="" target="_blank"></a> <a href="https://github.com/Shenyi-Z/ToCa" target="_blank"><img src="https://img.shields.io/github/stars/Shenyi-Z/ToCa?style=social"></a>

<a href="https://openreview.net/forum?id=UvMSKonce8" target="_blank"><img src="https://img.shields.io/badge/ICLR-2025-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" data-physical-first="false" aria-hidden="true"></span> Shaobo Wang, Hongxuan Tang, Mingyang Wang, Hongrui Zhang, <u>Xuyang Liu</u>, Weiya Li, Xuming Hu, Linfeng Zhang, &quot;**Gnothi Seauton: Empowering Faithful Self-Interpretability in Black-Box Transformers**&quot;. In *International Conference on Learning Representations (ICLR)*, 2025. [[paper](https://arxiv.org/pdf/2410.21815)] [[code](https://github.com/gszfwsb/AutoGnothi)] <a href="https://github.com/gszfwsb/AutoGnothi" target="_blank"><img src="https://img.shields.io/github/stars/gszfwsb/AutoGnothi?style=social"></a>

<a href="https://openreview.net/forum?id=yS1dUkQFnu" target="_blank"><img src="https://img.shields.io/badge/NeurIPS-2024-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" data-physical-first="false" aria-hidden="true"></span> Yi Xin<sup>\*</sup>, Siqi Luo<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Yuntao Du<sup>\*</sup>, Haodi Zhou, Xinyu Cheng, Christina Lee, and 10 more authors, &quot;**V-PETL Bench: A Unified Visual Parameter-Efficient Transfer Learning Benchmark**&quot;. In *Neural Information Processing Systems Datasets and Benchmarks Track (NeurlPS D&B Track)*, 2024. [[paper](https://openreview.net/forum?id=yS1dUkQFnu)][[page](https://v-petl-bench.github.io/)] [[code](https://github.com/synbol/Parameter-Efficient-Transfer-Learning-Benchmark)] [[poster](https://neurips.cc/virtual/2024/poster/97434)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:blknAaTinKkC' href="" target="_blank"></a> <a href="https://github.com/synbol/Parameter-Efficient-Transfer-Learning-Benchmark" target="_blank"><img src="https://img.shields.io/github/stars/synbol/Parameter-Efficient-Transfer-Learning-Benchmark?style=social"></a>

<!--
<a href="https://ieeexplore.ieee.org/document/10445945" target="_blank"><img src="https://img.shields.io/badge/ICASSP-2024-blue?style=flat-square"></a> <u>Xuyang Liu</u><sup>\*</sup>, Siteng Huang<sup>\*</sup>, Yachen Kang, Honggang Chen, Donglin Wang, &quot;**VGDiffZero: Text-to-image Diffusion Models Can Be Zero-shot Visual Grounders**&quot;. In *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)*, 2024. [[paper](https://arxiv.org/pdf/2309.01141.pdf)] [[code](https://github.com/xuyang-liu16/VGDiffZero)] [[poster](/files/ICASSP-2024-VGDiffZero-Poster.pdf)] <a href="https://github.com/xuyang-liu16/VGDiffZero" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/VGDiffZero?style=social"></a>

<a href="https://ieeexplore.ieee.org/document/10688132" target="_blank"><img src="https://img.shields.io/badge/ICME-2024-blue?style=flat-square"></a> Ting Liu<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Siteng Huang, Honggang Chen, Quanjun Yin, Long Qin, Donglin Wang, Yue Hu, &quot;**DARA: Domain- and Relation-aware Adapters Make Parameter-efficient Tuning for Visual Grounding**&quot;. In *IEEE International Conference on Multimedia & Expo (ICME)*, 2024. (<span style="color: red">**Oral**</span>) [[paper](https://arxiv.org/pdf/2405.06217)] [[code](https://github.com/liuting20/DARA)] [[poster](/files/ICME-2024-DARA-Poster.pdf)] <a href="https://github.com/liuting20/DARA" target="_blank"><img src="https://img.shields.io/github/stars/liuting20/DARA?style=social"></a> 
-->



<h3 class="pub-section-heading">Journal Papers</h3>

<a href="https://ieeexplore.ieee.org/document/10929057" target="_blank"><img src="https://img.shields.io/badge/TCSVT-2025-54b345?style=flat-square"></a><span class="pub-marker" data-first-author="true" data-physical-first="true" aria-hidden="true"></span> <u>Xuyang Liu</u><sup>\*</sup>, Ting Liu<sup>\*</sup>, Siteng Huang, Yi Xin, Yue Hu, Quanjun Yin, Donglin Wang, Yuanyuan Wu, Honggang Chen, &quot;**M2IST: Multi-Modal Interactive Side-Tuning for Efficient Referring Expression Comprehension**&quot;. *IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)*, 2025. [[paper](https://arxiv.org/pdf/2407.01131)] [[code](https://github.com/xuyang-liu16/M2IST)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:isC4tDSrTZIC' href="" target="_blank"></a>

<!-- 
<a href="https://ieeexplore.ieee.org/document/11206397" target="_blank"><img src="https://img.shields.io/badge/TCSS-2025-54b345?style=flat-square"></a> Junjie Chen, <u>Xuyang Liu</u>, Subin Huang, Linfeng Zhang, Hang Yu &quot;**Seeing Sarcasm Through Different Eyes: Analyzing Multimodal Sarcasm Perception in Large Vision-Language Models**&quot;. *IEEE Transactions on Computational Social Systems (TCSS)*, 2025. [[paper](https://arxiv.org/pdf/2503.12149)] [[code](https://github.com/CoderChen01/LVLMSarcasmAnalysis)] 

<a href="https://ieeexplore.ieee.org/document/10742110" target="_blank"><img src="https://img.shields.io/badge/TBC-2024-54b345?style=flat-square"></a> Xinying Lin, <u>Xuyang Liu</u>, Hong Yang, Xiaohai He, Honggang Chen, &quot;**Perception- and Fidelity-aware Reduced-Reference Super-Resolution Image Quality Assessment**&quot;. *IEEE Transactions on Broadcasting (TBC)*, 2024. [[paper](https://arxiv.org/pdf/2405.09472)] [[code](https://github.com/xinyouu/PFIQA)] 

<a href="https://www.sciencedirect.com/science/article/abs/pii/S0140366422002535" target="_blank"><img src="https://img.shields.io/badge/COMPUT COMMUN-2022-54b345?style=flat-square"></a> <u>Xuyang Liu</u>, &quot;**GLMLP-TRANS: A transportation mode detection model using lightweight sensors integrated in smartphones**&quot;. *Computer Communications*, 2022. [[paper](https://www.sciencedirect.com/science/article/abs/pii/S0140366422002535)] [[code](https://github.com/xuyang-liu16/GLMLP-TRANS)] 
-->



<h3 class="pub-section-heading">Preprints & Under Submission</h3>

<a href="https://arxiv.org/abs/2604.06330" target="_blank"><img src="https://img.shields.io/badge/arXiv-2604.06330-B31B1B?style=flat-square"></a><span class="pub-marker" data-first-author="false" data-physical-first="false" aria-hidden="true"></span> Yuzhe Chen, Jiale Cao, <u>Xuyang Liu</u>, Jin Xie, Aiping Yang, Yanwei Pang, &quot;**STDec: Spatio-Temporal Stability Guided Decoding for dLLMs**&quot;. *arXiv preprint arXiv:2604.06330*. [[paper](https://arxiv.org/pdf/2604.06330)] [[page](https://yzchen02.github.io/STDec/)]

<a href="https://arxiv.org/abs/2603.27650" target="_blank"><img src="https://img.shields.io/badge/arXiv-2603.27650-B31B1B?style=flat-square"></a><span class="pub-marker" data-first-author="true" data-physical-first="false" aria-hidden="true"></span> Xinying Lin, <u>Xuyang Liu</u><sup>†</sup>, Yiyu Wang, Teng Ma, Wenqi Ren, &quot;**V-CAST: Video Curvature-Aware Spatio-Temporal Pruning for Efficient Video Large Language Models**&quot;. *arXiv preprint arXiv:2603.27650*. [[paper](https://arxiv.org/pdf/2603.27650)] [[code](https://github.com/xinyouu/V-CAST)] [[page](https://xinyouu.github.io/V-CAST/)]


<!-- 
<a href="https://arxiv.org/abs/2510.14359" target="_blank"><img src="https://img.shields.io/badge/arXiv-2510.14359-B31B1B?style=flat-square"></a> Zichen Wen, Yiyu Wang, Chenfei Liao, Boxue Yang, Junxian Li, Weifeng Liu, Haocong He, Bolong Feng, <u>Xuyang Liu</u>, Yuanhuiyi Lyu, Xu Zheng, Xuming Hu, Linfeng Zhang &quot;**AI for Service: Proactive Assistance with AI Glasses**&quot;. *arXiv preprint arXiv:2510.14359*. [[paper](https://arxiv.org/pdf/2510.14359)] [[huggingface paper](https://huggingface.co/papers/2510.14359)]
-->

<a href="https://arxiv.org/abs/2505.19147" target="_blank"><img src="https://img.shields.io/badge/arXiv-2505.19147-B31B1B?style=flat-square"></a><span class="pub-marker" data-first-author="true" data-physical-first="true" aria-hidden="true"></span> <u>Xuyang Liu</u><sup>\*</sup>, Zichen Wen<sup>\*</sup>, Shaobo Wang<sup>\*</sup>, Junjie Chen, Zhishan Tao, and 10 more authors, &quot;**Shifting AI Efficiency From Model-Centric to Data-Centric Compression**&quot;. *arXiv preprint arXiv:2505.19147*. [[paper](https://arxiv.org/pdf/2505.19147)] [[project](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression)] [[huggingface paper](https://huggingface.co/papers/2505.19147)] [[Twitter@Rohan Paul](https://x.com/rohanpaul_ai/status/1936896115078525067?s=20)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:hMod-77fHWUC' href="" target="_blank"></a> <a href="https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/Awesome-Token-level-Model-Compression?style=social"></a> 

<a href="https://arxiv.org/abs/2405.14700" target="_blank"><img src="https://img.shields.io/badge/arXiv-2405.14700-B31B1B?style=flat-square"></a><span class="pub-marker" data-first-author="true" data-physical-first="false" aria-hidden="true"></span> Ting Liu<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Liangtao Shi, Zunnan Xu, Yue Hu, Siteng Huang, Yi Xin, Bineng Zhong, Donglin Wang, &quot;**Sparse-Tuning: Adapting Vision Transformers with Efficient Fine-tuning and Inference**&quot;. *arXiv preprint arXiv:2405.14700*. [[paper](https://arxiv.org/pdf/2405.14700)] [[github](https://github.com/liuting20/Sparse-Tuning)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:ZeXyd9-uunAC' href="" target="_blank"></a> <a href="https://github.com/liuting20/Sparse-Tuning" target="_blank"><img src="https://img.shields.io/github/stars/liuting20/Sparse-Tuning?style=social"></a>




## 🤗 Resources
Please find my full repositories on my [GitHub](https://github.com/xuyang-liu16) profile. <a href="https://github.com/xuyang-liu16" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16.svg?style=social" alt="GitHub"></a>

<div class="structured-grid" markdown="1">
<div class="structured-card" markdown="1">

### [Awesome Generation Acceleration](https://github.com/xuyang-liu16/Awesome-Generation-Acceleration) [![GitHub](https://img.shields.io/github/stars/xuyang-liu16/Awesome-Generation-Acceleration.svg?style=social)](https://github.com/xuyang-liu16/Awesome-Generation-Acceleration.git)
- **Duty:** Owner.
- **Description:** An open-source repository that curates a collection of recent awesome papers on AIGC acceleration.

</div>
<div class="structured-card" markdown="1">

### [Awesome Token-level Model Compression](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression) [![GitHub](https://img.shields.io/github/stars/xuyang-liu16/Awesome-Token-level-Model-Compression.svg?style=social)](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression.git)
- **Duty:** Owner.
- **Description:** An open-source repository that curates a collection of recent awesome papers on token-level model compression.

</div>
</div>


## 💻 Experiences

### Internships

<div class="timeline-list" markdown="1">
<div class="structured-card timeline-card" markdown="1">

<span class="timeline-date">Jul 2025 - Present</span>
<div markdown="1">

### Research Intern - **OPPO Research Institute, OPPO**, Shenzhen
- **Thesis:** *Video Understanding with Large Vision-Language Models*.
- **Supervisor:** Prof. [Lei Zhang](https://www4.comp.polyu.edu.hk/~cslzhang/).

</div>
</div>
<div class="structured-card timeline-card" markdown="1">

<span class="timeline-date">Apr 2025 - Jul 2025</span>
<div markdown="1">

### Research Intern - **Ant Security Lab, Ant Group**, Hangzhou
- **Thesis:** *Multi-modal Graphical User Interface (GUI) Agents*.

</div>
</div>
<div class="structured-card timeline-card" markdown="1">

<span class="timeline-date">Jul 2024 - Mar 2025</span>
<div markdown="1">

### Research Intern - **Taobao & Tmall Group, Alibaba Group**, Beijing
- **Thesis:** *Efficient Multi-modal Large Language Models*.

</div>
</div>
</div>
 
### Visiting

<div class="timeline-list" markdown="1">
<div class="structured-card timeline-card" markdown="1">

<span class="timeline-date">June 2024 - Present</span>
<div markdown="1">

### Research Assistant - **EPIC Lab, Shanghai Jiao Tong University**, Remote
- **Thesis:** *Efficient Multi-modal Large Language Models*.
- **Supervisor:** Prof. [Linfeng Zhang](http://www.zhanglinfeng.tech/).

</div>
</div>
<div class="structured-card timeline-card" markdown="1">

<span class="timeline-date">Mar 2023 - Sep 2023</span>
<div markdown="1">

### Visiting Student - **MiLab, Westlake University**, Hangzhou
- **Thesis:** *Efficient Transfer of Vision-language Models*.
- **Supervisors:** Dr. [Siteng Huang](https://kyonhuang.top/) and Prof. [Donglin Wang](https://en.westlake.edu.cn/faculty/donglin-wang.html).

</div>
</div>
</div>

## 📠 Services

### Conference Reviewer
<ul class="service-list">
  <li>International Conference on Learning Representations (<a href="https://iclr.cc/">ICLR</a>)</li>
  <li>International Conference on Machine Learning (<a href="https://icml.cc/">ICML</a>)</li>
  <li>Advances in Neural Information Processing Systems (<a href="https://neurips.cc/">NeurIPS</a>)</li>
  <li>AAAI Conference on Artificial Intelligence (<a href="https://aaai.org/conference/aaai/">AAAI</a>)</li>
  <li>ACM International Conference on Multimedia (<a href="https://2024.acmmm.org/">MM</a>)</li>
</ul>

### Journal Reviewer
<ul class="service-list">
  <li>IEEE Transactions on Image Processing (<a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=83">TIP</a>)</li>
  <li>IEEE Transactions on Circuits and Systems for Video Technology (<a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=76">TCSVT</a>)</li>
  <li>IEEE Transactions on Cybernetics (<a href="https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6221036">TCYB</a>)</li>
  <li>Computer Vision and Image Understanding (<a href="https://www.sciencedirect.com/journal/computer-vision-and-image-understanding">CVIU</a>)</li>
</ul>
