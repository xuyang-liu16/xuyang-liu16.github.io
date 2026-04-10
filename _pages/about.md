---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---


🌈 I am Xuyang Liu (刘旭洋), a third-year Master's student at [Sichuan University](https://en.scu.edu.cn/) <a href='https://en.scu.edu.cn/' target="_blank"><img src='./images/scu_logo.png' align="center" style='vertical-align: middle; width: 22px;'></a>, and an incoming PhD student at [PolyU](https://www.polyu.edu.hk/) <a href='https://www.polyu.edu.hk/' target="_blank"><img src='./images/polyu_logo.png' align="center" style='vertical-align: middle; width: 21px;'></a>, supervised by Prof. [Lei Zhang](https://www4.comp.polyu.edu.hk/~cslzhang/) (IEEE Fellow). I am also currently working as a research intern at [OPPO Research Institute](https://www.oppo.com/uk/) <a href='https://www.oppo.com/uk/' target="_blank"><img src='./images/oppo_logo.png' align="center" style='vertical-align: middle; width: 52px;'></a>. Previously, I have interned at [Ant Group](https://www.antgroup.com/en) <a href='https://www.antgroup.com/en' target="_blank"><img src='./images/alipay_logo.png' align="center" style='vertical-align: middle; width: 22px;'></a> focusing on GUI Agent, and [Taobao & Tmall Group](https://talent.taotian.com/) <a href='https://talent.taotian.com/' target="_blank"><img src='./images/taobao_logo.png' align="center" style='vertical-align: middle; width: 22px;'></a> working on Efficient VLMs. I've also spent half a year visiting [MiLAB](https://milab.westlake.edu.cn/) at [Westlake University](https://www.westlake.edu.cn/), supervised by Prof. [Donglin Wang](https://en.westlake.edu.cn/faculty/donglin-wang.html). I am fortunate to work closely with Dr. [Siteng Huang](https://kyonhuang.top/) from [DAMO Academy](https://damo.alibaba.com/) and Prof. [Linfeng Zhang](http://www.zhanglinfeng.tech/) from [SJTU](https://en.sjtu.edu.cn/).

📌 My research centers on **Efficient Large Vision-Language Models (LVLMs)**, including:

- 🖼️ **Image Understanding**: high-resolution understanding via context compression and fast decoding, including [GlobalCom<sup>2</sup>](https://arxiv.org/abs/2501.05179)<sub>[AAAI'26]</sub>, [V<sup>2</sup>Drop](https://arxiv.org/abs/2509.01552)<sub>[CVPR'26]</sub>, [FiCoCo](https://arxiv.org/abs/2411.17686)<sub>[AAAI'26]</sub>, and [MixKV](https://arxiv.org/abs/2510.20707)<sub>[ICLR'26]</sub>.
- 🎬 **Video Understanding**: long/audio-video, and streaming reasoning via efficient encoding and compression, including [VidCom<sup>2</sup>](https://arxiv.org/abs/2505.14454)<sub>[EMNLP'25]</sub>, [STC](https://arxiv.org/pdf/2512.00891)<sub>[CVPR'26]</sub>, [V-CAST](https://arxiv.org/abs/2603.27650), and [OmniSIFT](https://arxiv.org/abs/2602.04804).
- 🎨 **Content Generation**: lightweight and efficient AIGC via feature caching, pruning and fast decoding, including [ToCa](https://arxiv.org/abs/2410.05317)<sub>[ICLR'25]</sub>, [Flash-Unified](https://arxiv.org/abs/2603.15271)<sub>[CVPR'26 Findings]</sub>, and [STDec](https://arxiv.org/abs/2604.06330).
- ⚙️ **Efficiency Toolbox**: efficient transfer/fine-tuning and benchmarking for downstream task adaptation, including [M2IST](https://arxiv.org/abs/2407.01131)<sub>[TCSVT'25]</sub>, [V-PETL](https://openreview.net/forum?id=yS1dUkQFnu)<sub>[NeurIPS'24]</sub> and [AutoGnothi](https://arxiv.org/abs/2410.21815)<sub>[ICLR'25]</sub>.

📢 If you find these directions interesting, feel free to reach out via email: `liuxuyang@stu.scu.edu.cn`.



## 🔥 News

<div class="news-scroll" markdown="1">

* **2026.03.31** 🙌🙌 We release [V-CAST](https://arxiv.org/pdf/2603.27650), a **curvature-aware** spatio-temporal pruning framework for efficient long-context video inference. V-CAST achieves new SOTA of VideoLLM acceleration! [Code](https://github.com/xinyouu/V-CAST) is available!
* **2026.02.21** 🎊🎊 Four papers have been accepted by **CVPR 2026**, including token compression for VLMs via [V<sup>2</sup>Drop](https://arxiv.org/abs/2509.01552), efficient streaming video understanding via [STC](https://arxiv.org/abs/2512.00891), and token compression for autonomous driving via [Prune2Drive](https://arxiv.org/abs/2508.13305) to the main conference, and [Flash-Unified](https://arxiv.org/abs/2603.15271) to the findings! 
* **2026.01.26** 🎊🎊 Two papers have been accepted by **ICLR 2026**, including fast decoding for VLM/LLM via [MixKV](https://arxiv.org/abs/2510.20707) and the first safety study of dLLMs [DIJA](https://arxiv.org/abs/2507.11097)! Congratulations to all collaborators!
* **2025.11.08** 🎊🎊 Three papers have been accepted by **AAAI 2026**, including two LVLM acceleration methods [GlobalCom<sup>2</sup>](https://arxiv.org/abs/2501.05179) and [FiCoCo](https://arxiv.org/abs/2411.17686), and a RL-based GUI grounding training framework [GUI-G<sup>2</sup>](https://arxiv.org/abs/2507.15846)!
* **2025.08.21** 🎊🎊 One first author paper [VidCom<sup>2</sup>](https://arxiv.org/abs/2505.14454) about plug-and-play inference acceleration for VideoLLMs has been accepted by **EMNLP 2025** main conference! [Code](https://github.com/xuyang-liu16/VidCom2) is available!
* **2025.05.27** 🙌🙌 We release a new [paper](https://arxiv.org/abs/2505.19147), pointing to **shifting AI efficiency from model-centric to data-centric compression**. [Project](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression) is available! Our paper is honored to be the [#2 Paper of the day](https://huggingface.co/papers/2505.19147)!
* **2025.03.11** 🎊🎊 One first author paper ([M2IST](https://arxiv.org/abs/2407.01131)) about parameter-, memory-, and time-efficient fine-tuning for referring expression comprehension has been accepted by IEEE Transactions on Circuits and Systems for Video Technology (**TCSVT**)!
* **2025.02.22** 🎊🎊 Two papers ([ToCa](https://arxiv.org/abs/2410.05317) and [AutoGnothi](https://arxiv.org/abs/2410.21815)) have been accepted by **ICLR 2025**! Congratulations to all collaborators!
* **2024.09.26** 🎊🎊 One co-first author paper ([V-PETL](https://openreview.net/forum?id=yS1dUkQFnu)) about unified visual parameter-efficient transfer learning benchmark has been accepted by **NeurIPS 2024**!

</div>


## 📝 Publications 

Full publications are on my [Google Scholar](https://scholar.google.com/citations?user=9VhMC1QAAAAJ&hl=en) profile. *: Equal contribution. †: Project leader. <a href="https://scholar.google.com/citations?user=9VhMC1QAAAAJ" target="_blank"><img src="https://img.shields.io/badge/dynamic/json?label=Paper%20Citations&query=total_citations&url=https%3A%2F%2Fcse.bth.se%2F~fer%2Fgooglescholar-api%2Fgooglescholar.php%3Fuser%3D9VhMC1QAAAAJ&logo=googlescholar&style=social" alt="Google Scholar"></a> 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/MixKV_teaser.png' alt="MixKV teaser" width="100%"><p class="paper-caption"><i>💡 The <strong>first</strong> to identify <strong>heterogeneous head-wise redundancy</strong> in the KV cache of both LVLMs and LLMs.</i></p></div></div>
<div class='paper-box-text' markdown="1">

[**Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models**](https://openreview.net/forum?id=B2iqbCQviR)

<u>Xuyang Liu</u><sup>*</sup>, Xiyan Gui<sup>*</sup>, Yuchao Zhang, Linfeng Zhang

- Works with diverse LVLMs and LLMs, including LLaVA, Qwen-VL, InternVL, Llama, and Mistral series.
- Integrates with existing compressors (e.g., SnapKV, AdaKV, SparseMM) and consistently improves their performance.
- Delivers accuracy gains (average of **+5.1%** across 5 tasks) without sacrificing speed or memory efficiency.

<div style="display: inline">
  <a href="https://arxiv.org/pdf/2510.20707"><strong>[paper]</strong></a>
  <a href="https://github.com/xuyang-liu16/MixKV"><strong>[code]</strong></a>
  <a href="https://xuyang-liu16.github.io/MixKV/"><strong>[page]</strong></a>
  <a href="http://xhslink.com/o/9VKjxY3ZWbW"><strong>[Xiaohongshu]</strong></a>
  <a href="https://mp.weixin.qq.com/s/O1mIsIt6LSTZhAF536vGiA"><strong>[量子位]</strong></a>
  <a href="https://mp.weixin.qq.com/s/rMKnBVWCwl6lq9eRdpjvdw"><strong>[52CV]</strong></a>
</div>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025</div><img src='images/VidCom2_teaser.png' alt="VidCom2 teaser" width="100%"><p class="paper-caption"><i>⚡ The <strong>first</strong> token compression framework for VideoLLMs featuring <strong>dynamic frame budget allocation</strong>.</i></p></div></div>
<div class='paper-box-text' markdown="1">

[**Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models**](https://aclanthology.org/2025.emnlp-main.98/)

<u>Xuyang Liu</u><sup>*</sup>, Yiyu Wang<sup>*</sup>, Junpeng Ma, Linfeng Zhang

- Compatible with major VideoLLMs and OmniLLMs, including LLaVA, Qwen-VL, and Qwen-Omni series.
- Uses only **25%** of visual tokens while preserving **99.6%** performance of LLaVA-OV.
- Reduces LLaVA-OV LLM generation time by **70.8%** and overall latency by **43.0%**.

<div style="display: inline">
  <a href="https://arxiv.org/pdf/2505.14454"><strong>[paper]</strong></a>
  <a href="https://github.com/xuyang-liu16/VidCom2"><strong>[code]</strong></a>
  <a href="https://xuyang-liu16.github.io/VidCom2/"><strong>[page]</strong></a>
  <a href="http://xhslink.com/o/7SMiHSgXFFU"><strong>[Xiaohongshu]</strong></a>
  <a href="https://www.jiqizhixin.com/articles/2025-12-15-6"><strong>[机器之心]</strong></a>
  <a href="https://mp.weixin.qq.com/s/hQhEPlBWd4noVGSOWT4_XQ"><strong>[PaperWeekly]</strong></a>
  <a href="/files/EMNLP-2025-main-262.pdf"><strong>[slides]</strong></a>
  <a href="/files/EMNLP-2025-main-262-Poster.pdf"><strong>[poster]</strong></a>
  <a href="https://underline.io/events/502/posters/20833/poster/129850-video-compression-commander-plug-and-play-inference-acceleration-for-video-large-language-models"><strong>[video]</strong></a>
</div>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='images/GlobalCom2_teaser.png' alt="GlobalCom2 teaser" width="100%"><p class="paper-caption"><i>📊 The <strong>first</strong> to systematically analyze token compression in HR-LVLMs with <strong>adaptive crop budget allocation</strong>. </i></p></div></div>
<div class='paper-box-text' markdown="1">

[**Global Compression Commander: Plug-and-Play Inference Acceleration for High-Resolution Large Vision-Language Models**](https://arxiv.org/abs/2501.05179)

<u>Xuyang Liu</u>, Ziming Wang, Junjie Chen, Yuhang Han, Yingyao Wang, Jiale Yuan, Jun Song, Siteng Huang, Honggang Chen

- Compatible with major HR-LVLMs, including LLaVA-NeXT and LLaVA-OV.
- Uses only **10%** of visual tokens while maintaining above **90%** performance across **10** tasks.
- Reduces FLOPs and peak memory to **9.1%** and **60%**, and achieves 1.8x throughput.

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
  .pub-section-heading.is-hidden {
    display: none;
  }
</style>

<div class="pub-filters" id="pub-filters" aria-label="Publication filters">
  <button type="button" class="pub-filter-btn is-active" data-filter="all">All</button>
  <button type="button" class="pub-filter-btn" data-filter="first-author">Core</button>
</div>

<div class="pub-highlight" id="pub-highlight">🚩 Highlight: ICLR: 4, NeurIPS: 1, CVPR: 4, AAAI: 3, EMNLP: 1.</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    var filterRoot = document.getElementById("pub-filters");
    var highlightNode = document.getElementById("pub-highlight");
    if (!filterRoot) return;

    var buttons = Array.prototype.slice.call(filterRoot.querySelectorAll(".pub-filter-btn"));
    var headings = Array.prototype.slice.call(document.querySelectorAll(".pub-section-heading"));
    var highlightOrder = ["ICLR", "NeurIPS", "CVPR", "AAAI", "EMNLP"];
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

    function getVenue(item) {
      var badge = item.querySelector("a img");
      if (!badge) return null;

      var source = badge.getAttribute("src") || "";
      var match = source.match(/badge\/(ICLR|NeurIPS|CVPR|AAAI|EMNLP)-/i);
      return match ? match[1] : null;
    }

    function updateHighlight() {
      if (!highlightNode) return;

      var counts = {
        ICLR: 0,
        NeurIPS: 0,
        CVPR: 0,
        AAAI: 0,
        EMNLP: 0
      };

      sections.forEach(function (section) {
        section.items.forEach(function (item) {
          if (item.classList.contains("is-hidden")) return;

          var venue = getVenue(item);
          if (venue && Object.prototype.hasOwnProperty.call(counts, venue)) {
            counts[venue] += 1;
          }
        });
      });

      var summary = highlightOrder
        .map(function (venue) {
          return venue + ": " + counts[venue];
        })
        .join(", ");

      highlightNode.textContent = "🚩 Highlight: " + summary + ".";
    }

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
          var shouldShow = filter === "all" || isFirstAuthor;

          item.classList.toggle("is-hidden", !shouldShow);
          if (shouldShow) visibleCount += 1;
        });

        section.heading.classList.toggle("is-hidden", visibleCount === 0);
      });

      updateHighlight();
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

<a href="https://arxiv.org/abs/2512.00891" target="_blank"><img src="https://img.shields.io/badge/CVPR-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> Yiyu Wang<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*,†</sup>, Xiyan Gui, Xinying Lin, Boxue Yang, Chenfei Liao, Tailai Chen, Linfeng Zhang, &quot;**Accelerating Streaming Video Large Language Models via Hierarchical Token Compression**&quot;. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2026. [[paper](https://arxiv.org/pdf/2512.00891)] [[code](https://github.com/lern-to-write/STC)] [[Xiaohongshu](http://xhslink.com/o/5Vm008DxkkH 
)] [[PaperWeekly](https://mp.weixin.qq.com/s/PsNkR28yIFXqAQmAb62Yrg
)] <a href="https://github.com/lern-to-write/STC" target="_blank"><img src="https://img.shields.io/github/stars/lern-to-write/STC?style=social"></a>

<a href="https://arxiv.org/abs/2509.01552" target="_blank"><img src="https://img.shields.io/badge/CVPR-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> Junjie Chen<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*,†</sup>, Zichen Wen, Yiyu Wang, Siteng Huang, Honggang Chen, &quot;**Variation-aware Vision Token Dropping for Faster Large Vision-Language Models**&quot;. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2026. [[paper](https://arxiv.org/pdf/2509.01552)] [[code](https://github.com/xuyang-liu16/V2Drop)] [[机器之心](https://mp.weixin.qq.com/s/5dGS58sg29qLA4mKOLS9bQ)] [[52CV](https://mp.weixin.qq.com/s/C2BO_lamuQcLQW5JedfvFg)] <a href="https://github.com/xuyang-liu16/V2Drop" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/V2Drop?style=social"></a>

<a href="https://arxiv.org/abs/2508.13305" target="_blank"><img src="https://img.shields.io/badge/CVPR-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" aria-hidden="true"></span> Minhao Xiong, Zichen Wen, Zhuangcheng Gu, <u>Xuyang Liu</u>, Rui Zhang, Hengrui Kang, Jiabing Yang, Junyuan Zhang, Weijia Li, Conghui He, Yafei Wang, Linfeng Zhang, &quot;**Prune2Drive: A Plug-and-Play Framework for Accelerating Vision-Language Models in Autonomous Driving**&quot;. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2026. [[paper](https://arxiv.org/pdf/2508.13305)] [[code](https://github.com/MinhaoXiong/Prune2Drive)]

<a href="https://arxiv.org/abs/2603.15271" target="_blank"><img src="https://img.shields.io/badge/CVPR-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" aria-hidden="true"></span> Junlong Ke, Zichen Wen, Boxue Yang, Yantai Yang, <u>Xuyang Liu</u>, Chenfei Liao, Zhaorun Chen, Shaobo Wang, Linfeng Zhang, &quot;**Flash-Unified: A Training-Free and Task-Aware Acceleration Framework for Native Unified Models**&quot;. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Findings*, 2026. [[paper](https://arxiv.org/pdf/2603.15271)] [[code](https://github.com/Rirayh/FlashU)]

<a href="https://openreview.net/forum?id=B2iqbCQviR" target="_blank"><img src="https://img.shields.io/badge/ICLR-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> <u>Xuyang Liu</u><sup>\*</sup>, Xiyan Gui<sup>\*</sup>, Yuchao Zhang, Linfeng Zhang, &quot;**Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models**&quot;. In *International Conference on Learning Representations (ICLR)*, 2026. [[paper](https://arxiv.org/pdf/2510.20707)] [[code](https://github.com/xuyang-liu16/MixKV)] [[page](https://xuyang-liu16.github.io/MixKV/)] [[Xiaohongshu](http://xhslink.com/o/9VKjxY3ZWbW)] [[量子位](https://mp.weixin.qq.com/s/O1mIsIt6LSTZhAF536vGiA)] [[52CV](https://mp.weixin.qq.com/s/rMKnBVWCwl6lq9eRdpjvdw)] <a href="https://github.com/xuyang-liu16/MixKV" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/MixKV?style=social"></a>

<a href="https://openreview.net/forum?id=rIPeatvPy3" target="_blank"><img src="https://img.shields.io/badge/ICLR-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" aria-hidden="true"></span> Zichen Wen, Jiashu Qu, Dongrui Liu, Zhiyuan Liu, Ruixi Wu, Yicun Yang, Xiangqi Jin, Haoyun Xu, <u>Xuyang Liu</u>, Weijia Li, Chaochao Lu, Jing Shao, Conghui He, Linfeng Zhang, &quot;**The Devil behind the mask: An emergent safety vulnerability of Diffusion LLMs**&quot;. In *International Conference on Learning Representations (ICLR)*, 2026. [[paper](https://arxiv.org/pdf/2507.11097)] [[code](https://github.com/ZichenWen1/DIJA)] [[huggingface paper](https://huggingface.co/papers/2507.11097)] [[量子位](https://mp.weixin.qq.com/s/nfyZFXN7ku07_9tTzG-W9Q)] <a href="https://github.com/ZichenWen1/DIJA" target="_blank"><img src="https://img.shields.io/github/stars/ZichenWen1/DIJA?style=social"></a> 

<a href="https://ojs.aaai.org/index.php/AAAI/article/view/37673" target="_blank"><img src="https://img.shields.io/badge/AAAI-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> <u>Xuyang Liu</u>, Ziming Wang, Junjie Chen, Yuhang Han, Yingyao Wang, Jiale Yuan, Jun Song, Siteng Huang, Honggang Chen, &quot;**Global Compression Commander: Plug-and-Play Inference Acceleration for High-Resolution Large Vision-Language Models**&quot;. In *Proceedings of the 40th AAAI Conference on Artificial Intelligence*, 2026. [[paper](https://arxiv.org/pdf/2501.05179)] [[code](https://github.com/xuyang-liu16/GlobalCom2)] [[poster](/files/AAAI-2026-GlobalCom2-Poster.pdf)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:yD5IFk8b50cC' href="" target="_blank"></a>
 <a href="https://github.com/xuyang-liu16/GlobalCom2" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/GlobalCom2?style=social"></a>

<a href="https://ojs.aaai.org/index.php/AAAI/article/view/42460" target="_blank"><img src="https://img.shields.io/badge/AAAI-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> Yuhang Han<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Zihan Zhang, Pengxiang Ding, Junjie Chen, Donglin Wang, Honggang Chen, Qingsen Yan, Siteng Huang, &quot;**Filter, Correlate, Compress: Training-Free Token Reduction for MLLM Acceleration**&quot;. In *Proceedings of the 40th AAAI Conference on Artificial Intelligence*, 2026. [[paper](https://arxiv.org/pdf/2411.17686)] [[page](https://ficoco-accelerate.github.io/)] [[code](https://github.com/kawhiiiileo/FiCoCo)][[poster](/files/AAAI-2026-Poster-FiCoCo.pdf)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:cFHS6HbyZ2cC' href="" target="_blank"></a> <a href="https://github.com/kawhiiiileo/FiCoCo" target="_blank"><img src="https://img.shields.io/github/stars/kawhiiiileo/FiCoCo?style=social"></a>

<a href="https://ojs.aaai.org/index.php/AAAI/article/view/40606" target="_blank"><img src="https://img.shields.io/badge/AAAI-2026-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" aria-hidden="true"></span> Fei Tang, Zhangxuan Gu, Zhengxi Lu, <u>Xuyang Liu</u>, Shuheng Shen, Changhua Meng, Wen Wang, Wenqi Zhang, Yongliang Shen, Weiming Lu, Jun Xiao, Yueting Zhuang, &quot;**GUI-G<sup>2</sup>: Gaussian Reward Modeling for GUI Grounding**&quot;. In *Proceedings of the 40th AAAI Conference on Artificial Intelligence*, 2026. [[paper](https://arxiv.org/pdf/2507.15846)] [[code](https://github.com/zju-real/GUI-G2)] [[huggingface paper](https://huggingface.co/papers/2507.15846)] [[page](https://zju-real.github.io/GUI-G2)] [[机器之心](https://mp.weixin.qq.com/s/DRMtB-o9X_CzEFGkxw0Ycw)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:ns9cj8rnVeAC' href="" target="_blank"></a> <a href="https://github.com/zju-real/GUI-G2" target="_blank"><img src="https://img.shields.io/github/stars/zju-real/GUI-G2?style=social"></a>

<a href="https://aclanthology.org/2025.emnlp-main.98/" target="_blank"><img src="https://img.shields.io/badge/EMNLP-2025-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> <u>Xuyang Liu</u><sup>\*</sup>, Yiyu Wang<sup>\*</sup>, Junpeng Ma, Linfeng Zhang, &quot;**Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models**&quot;. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2025. [[paper](https://arxiv.org/pdf/2505.14454)] [[code](https://github.com/xuyang-liu16/VidCom2)] [[page](https://xuyang-liu16.github.io/VidCom2/)] [[Xiaohongshu](http://xhslink.com/o/7SMiHSgXFFU)] [[机器之心](https://www.jiqizhixin.com/articles/2025-12-15-6)] [[PaperWeekly](https://mp.weixin.qq.com/s/hQhEPlBWd4noVGSOWT4_XQ)] [[slides](/files/EMNLP-2025-main-262.pdf)] [[poster](/files/EMNLP-2025-main-262-Poster.pdf)] [[video](https://underline.io/events/502/posters/20833/poster/129850-video-compression-commander-plug-and-play-inference-acceleration-for-video-large-language-models)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:a0OBvERweLwC' href="" target="_blank"></a> <a href="https://github.com/xuyang-liu16/VidCom2" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/VidCom2?style=social"></a>

<a href="https://openreview.net/forum?id=yYZbZGo4ei" target="_blank"><img src="https://img.shields.io/badge/ICLR-2025-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> Chang Zou<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Ting Liu, Siteng Huang, Linfeng Zhang, &quot;**Accelerating Diffusion Transformers with Token-wise Feature Caching**&quot;. In *International Conference on Learning Representations (ICLR)*, 2025. [[paper](https://arxiv.org/pdf/2410.05317)] [[page](https://toca2024.github.io/ToCa/)] [[code](https://github.com/Shenyi-Z/ToCa)] [[量子位](https://mp.weixin.qq.com/s/ZqVWslSEdjX00VMf6RqtcA)] [[poster](/files/ICLR-2025-ToCa-Poster.pdf)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:TQgYirikUcIC' href="" target="_blank"></a> <a href="https://github.com/Shenyi-Z/ToCa" target="_blank"><img src="https://img.shields.io/github/stars/Shenyi-Z/ToCa?style=social"></a>

<a href="https://openreview.net/forum?id=UvMSKonce8" target="_blank"><img src="https://img.shields.io/badge/ICLR-2025-blue?style=flat-square"></a><span class="pub-marker" data-first-author="false" aria-hidden="true"></span> Shaobo Wang, Hongxuan Tang, Mingyang Wang, Hongrui Zhang, <u>Xuyang Liu</u>, Weiya Li, Xuming Hu, Linfeng Zhang, &quot;**Gnothi Seauton: Empowering Faithful Self-Interpretability in Black-Box Transformers**&quot;. In *International Conference on Learning Representations (ICLR)*, 2025. [[paper](https://arxiv.org/pdf/2410.21815)] [[code](https://github.com/gszfwsb/AutoGnothi)] <a href="https://github.com/gszfwsb/AutoGnothi" target="_blank"><img src="https://img.shields.io/github/stars/gszfwsb/AutoGnothi?style=social"></a>

<a href="https://openreview.net/forum?id=yS1dUkQFnu" target="_blank"><img src="https://img.shields.io/badge/NeurIPS-2024-blue?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> Yi Xin<sup>\*</sup>, Siqi Luo<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Yuntao Du<sup>\*</sup>, Haodi Zhou, Xinyu Cheng, Christina Lee, and 10 more authors, &quot;**V-PETL Bench: A Unified Visual Parameter-Efficient Transfer Learning Benchmark**&quot;. In *Neural Information Processing Systems Datasets and Benchmarks Track (NeurlPS D&B Track)*, 2024. [[paper](https://openreview.net/forum?id=yS1dUkQFnu)][[page](https://v-petl-bench.github.io/)] [[code](https://github.com/synbol/Parameter-Efficient-Transfer-Learning-Benchmark)] [[poster](https://neurips.cc/virtual/2024/poster/97434)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:blknAaTinKkC' href="" target="_blank"></a> <a href="https://github.com/synbol/Parameter-Efficient-Transfer-Learning-Benchmark" target="_blank"><img src="https://img.shields.io/github/stars/synbol/Parameter-Efficient-Transfer-Learning-Benchmark?style=social"></a>

<!--
<a href="https://ieeexplore.ieee.org/document/10445945" target="_blank"><img src="https://img.shields.io/badge/ICASSP-2024-blue?style=flat-square"></a> <u>Xuyang Liu</u><sup>\*</sup>, Siteng Huang<sup>\*</sup>, Yachen Kang, Honggang Chen, Donglin Wang, &quot;**VGDiffZero: Text-to-image Diffusion Models Can Be Zero-shot Visual Grounders**&quot;. In *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)*, 2024. [[paper](https://arxiv.org/pdf/2309.01141.pdf)] [[code](https://github.com/xuyang-liu16/VGDiffZero)] [[poster](/files/ICASSP-2024-VGDiffZero-Poster.pdf)] <a href="https://github.com/xuyang-liu16/VGDiffZero" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/VGDiffZero?style=social"></a>

<a href="https://ieeexplore.ieee.org/document/10688132" target="_blank"><img src="https://img.shields.io/badge/ICME-2024-blue?style=flat-square"></a> Ting Liu<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Siteng Huang, Honggang Chen, Quanjun Yin, Long Qin, Donglin Wang, Yue Hu, &quot;**DARA: Domain- and Relation-aware Adapters Make Parameter-efficient Tuning for Visual Grounding**&quot;. In *IEEE International Conference on Multimedia & Expo (ICME)*, 2024. (<span style="color: red">**Oral**</span>) [[paper](https://arxiv.org/pdf/2405.06217)] [[code](https://github.com/liuting20/DARA)] [[poster](/files/ICME-2024-DARA-Poster.pdf)] <a href="https://github.com/liuting20/DARA" target="_blank"><img src="https://img.shields.io/github/stars/liuting20/DARA?style=social"></a> 
-->



<h3 class="pub-section-heading">Journal Papers</h3>

<a href="https://ieeexplore.ieee.org/document/10929057" target="_blank"><img src="https://img.shields.io/badge/TCSVT-2025-54b345?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> <u>Xuyang Liu</u><sup>\*</sup>, Ting Liu<sup>\*</sup>, Siteng Huang, Yi Xin, Yue Hu, Quanjun Yin, Donglin Wang, Yuanyuan Wu, Honggang Chen, &quot;**M2IST: Multi-Modal Interactive Side-Tuning for Efficient Referring Expression Comprehension**&quot;. *IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)*, 2025. [[paper](https://arxiv.org/pdf/2407.01131)] [[code](https://github.com/xuyang-liu16/M2IST)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:isC4tDSrTZIC' href="" target="_blank"></a>

<!-- 
<a href="https://ieeexplore.ieee.org/document/11206397" target="_blank"><img src="https://img.shields.io/badge/TCSS-2025-54b345?style=flat-square"></a> Junjie Chen, <u>Xuyang Liu</u>, Subin Huang, Linfeng Zhang, Hang Yu &quot;**Seeing Sarcasm Through Different Eyes: Analyzing Multimodal Sarcasm Perception in Large Vision-Language Models**&quot;. *IEEE Transactions on Computational Social Systems (TCSS)*, 2025. [[paper](https://arxiv.org/pdf/2503.12149)] [[code](https://github.com/CoderChen01/LVLMSarcasmAnalysis)] 

<a href="https://ieeexplore.ieee.org/document/10742110" target="_blank"><img src="https://img.shields.io/badge/TBC-2024-54b345?style=flat-square"></a> Xinying Lin, <u>Xuyang Liu</u>, Hong Yang, Xiaohai He, Honggang Chen, &quot;**Perception- and Fidelity-aware Reduced-Reference Super-Resolution Image Quality Assessment**&quot;. *IEEE Transactions on Broadcasting (TBC)*, 2024. [[paper](https://arxiv.org/pdf/2405.09472)] [[code](https://github.com/xinyouu/PFIQA)] 

<a href="https://www.sciencedirect.com/science/article/abs/pii/S0140366422002535" target="_blank"><img src="https://img.shields.io/badge/COMPUT COMMUN-2022-54b345?style=flat-square"></a> <u>Xuyang Liu</u>, &quot;**GLMLP-TRANS: A transportation mode detection model using lightweight sensors integrated in smartphones**&quot;. *Computer Communications*, 2022. [[paper](https://www.sciencedirect.com/science/article/abs/pii/S0140366422002535)] [[code](https://github.com/xuyang-liu16/GLMLP-TRANS)] 
-->



<h3 class="pub-section-heading">Preprints & Under Submission</h3>

<a href="https://arxiv.org/abs/2604.06330" target="_blank"><img src="https://img.shields.io/badge/arXiv-2604.06330-B31B1B?style=flat-square"></a><span class="pub-marker" data-first-author="false" aria-hidden="true"></span> Yuzhe Chen, Jiale Cao, <u>Xuyang Liu</u>, Jin Xie, Aiping Yang, Yanwei Pang, &quot;**STDec: Spatio-Temporal Stability Guided Decoding for dLLMs**&quot;. *arXiv preprint arXiv:2604.06330*. [[paper](https://arxiv.org/pdf/2604.06330)] [[page](https://yzchen02.github.io/STDec/)]

<a href="https://arxiv.org/abs/2603.27650" target="_blank"><img src="https://img.shields.io/badge/arXiv-2603.27650-B31B1B?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> Xinying Lin, <u>Xuyang Liu</u><sup>†</sup>, Yiyu Wang, Teng Ma, Wenqi Ren, &quot;**V-CAST: Video Curvature-Aware Spatio-Temporal Pruning for Efficient Video Large Language Models**&quot;. *arXiv preprint arXiv:2603.27650*. [[paper](https://arxiv.org/pdf/2603.27650)] [[code](https://github.com/xinyouu/V-CAST)] [[page](https://xinyouu.github.io/V-CAST/)]

<a href="https://arxiv.org/abs/2602.04804" target="_blank"><img src="https://img.shields.io/badge/arXiv-2602.04804-B31B1B?style=flat-square"></a><span class="pub-marker" data-first-author="false" aria-hidden="true"></span> Yue Ding, Yiyan Ji, Jungang Li, <u>Xuyang Liu</u>, Xinlong Chen, and 10 more authors, &quot;**OmniSIFT: Modality-Asymmetric Token Compression for Efficient Omni-modal Large Language Models**&quot;. *arXiv preprint arXiv:2602.04804*. [[paper](https://arxiv.org/pdf/2602.04804)] [[huggingface paper](https://huggingface.co/papers/2602.04804)]


<!-- 
<a href="https://arxiv.org/abs/2510.14359" target="_blank"><img src="https://img.shields.io/badge/arXiv-2510.14359-B31B1B?style=flat-square"></a> Zichen Wen, Yiyu Wang, Chenfei Liao, Boxue Yang, Junxian Li, Weifeng Liu, Haocong He, Bolong Feng, <u>Xuyang Liu</u>, Yuanhuiyi Lyu, Xu Zheng, Xuming Hu, Linfeng Zhang &quot;**AI for Service: Proactive Assistance with AI Glasses**&quot;. *arXiv preprint arXiv:2510.14359*. [[paper](https://arxiv.org/pdf/2510.14359)] [[huggingface paper](https://huggingface.co/papers/2510.14359)]
-->

<a href="https://arxiv.org/abs/2505.19147" target="_blank"><img src="https://img.shields.io/badge/arXiv-2505.19147-B31B1B?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> <u>Xuyang Liu</u><sup>\*</sup>, Zichen Wen<sup>\*</sup>, Shaobo Wang<sup>\*</sup>, Junjie Chen, Zhishan Tao, and 10 more authors, &quot;**Shifting AI Efficiency From Model-Centric to Data-Centric Compression**&quot;. *arXiv preprint arXiv:2505.19147*. [[paper](https://arxiv.org/pdf/2505.19147)] [[project](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression)] [[huggingface paper](https://huggingface.co/papers/2505.19147)] [[Twitter@Rohan Paul](https://x.com/rohanpaul_ai/status/1936896115078525067?s=20)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:hMod-77fHWUC' href="" target="_blank"></a> <a href="https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/Awesome-Token-level-Model-Compression?style=social"></a> 

<a href="https://arxiv.org/abs/2405.14700" target="_blank"><img src="https://img.shields.io/badge/arXiv-2405.14700-B31B1B?style=flat-square"></a><span class="pub-marker" data-first-author="true" aria-hidden="true"></span> Ting Liu<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Liangtao Shi, Zunnan Xu, Yue Hu, Siteng Huang, Yi Xin, Bineng Zhong, Donglin Wang, &quot;**Sparse-Tuning: Adapting Vision Transformers with Efficient Fine-tuning and Inference**&quot;. *arXiv preprint arXiv:2405.14700*. [[paper](https://arxiv.org/pdf/2405.14700)] [[github](https://github.com/liuting20/Sparse-Tuning)] <a class='paper_citations_badges' data='9VhMC1QAAAAJ:ZeXyd9-uunAC' href="" target="_blank"></a> <a href="https://github.com/liuting20/Sparse-Tuning" target="_blank"><img src="https://img.shields.io/github/stars/liuting20/Sparse-Tuning?style=social"></a>



## 🤗 Resources
Please find my full repositories on my [GitHub](https://github.com/xuyang-liu16) profile. <a href="https://github.com/xuyang-liu16" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16.svg?style=social" alt="GitHub"></a>

* [Awesome Generation Acceleration](https://github.com/xuyang-liu16/Awesome-Generation-Acceleration) [![GitHub](https://img.shields.io/github/stars/xuyang-liu16/Awesome-Generation-Acceleration.svg?style=social)](https://github.com/xuyang-liu16/Awesome-Generation-Acceleration.git)
  * Duty: Owner.
  * Description: An open-source repository that curates a collection of recent awesome papers on AIGC acceleration.
 
* [Awesome Token-level Model Compression](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression) [![GitHub](https://img.shields.io/github/stars/xuyang-liu16/Awesome-Token-level-Model-Compression.svg?style=social)](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression.git)
  * Duty: Owner.
  * Description: An open-source repository that curates a collection of recent awesome papers on token-level model compression.


## 💻 Experiences

### Internships

* Research Intern - **OPPO Research Institute, OPPO**, Shenzhen
  * Time: Jul 2025 - Present.
  * Thesis: *Video Understanding with Large Vision-Language Models*.
  * Supervisor: Prof. [Lei Zhang](https://www4.comp.polyu.edu.hk/~cslzhang/).

* Research Intern - **Ant Security Lab, Ant Group**, Hangzhou
  * Time: Apr 2025 - Jul 2025.
  * Thesis: *Multi-modal Graphical User Interface (GUI) Agents*.

* Research Intern - **Taobao & Tmall Group, Alibaba Group**, Beijing
  * Time: Jul 2024 - Mar 2025.
  * Thesis: *Efficient Multi-modal Large Language Models*.
 
### Visiting

* Research Assistant - **EPIC Lab, Shanghai Jiao Tong University**, Remote
  * Time: June 2024 - Present.
  * Thesis: *Efficient Multi-modal Large Language Models*.
  * Supervisor: Prof. [Linfeng Zhang](http://www.zhanglinfeng.tech/).
  
* Visiting Student - **MiLab, Westlake University**, Hangzhou
  * Time: Mar 2023 - Sep 2023.
  * Thesis: *Efficient Transfer of Vision-language Models*.
  * Supervisors: Dr. [Siteng Huang](https://kyonhuang.top/) and Prof. [Donglin Wang](https://en.westlake.edu.cn/faculty/donglin-wang.html).

## 🎤 Talks

* **2025.06.10**: [PolyU NLP Group](https://polyunlp.github.io/) directed by Prof. [Wenjie Li](https://www4.comp.polyu.edu.hk/~cswjli/): **Shifting AI Efficiency From Model-Centric to Data-Centric Compression**. [[slides](/files/Talk@PolyUNLP.pdf)]


## 📠 Services

### Conference Reviewer
* International Conference on Learning Representations ([ICLR](https://iclr.cc/))
* International Conference on Machine Learning ([ICML](https://icml.cc/))
* Advances in Neural Information Processing Systems ([NeurIPS](https://neurips.cc/))
* AAAI Conference on Artificial Intelligence ([AAAI](https://aaai.org/conference/aaai/))
* ACM International Conference on Multimedia ([MM](https://2024.acmmm.org/))

### Journal Reviewer
* IEEE Transactions on Image Processing ([TIP](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=83))
* IEEE Transactions on Circuits and Systems for Video Technology ([TCSVT](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=76))
* Computer Vision and Image Understanding ([CVIU](https://www.sciencedirect.com/journal/computer-vision-and-image-understanding))
