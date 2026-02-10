---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---


🌈 I am Xuyang Liu (刘旭洋), a third-year Master's student at [Sichuan University](https://en.scu.edu.cn/) <a href='https://en.scu.edu.cn/' target="_blank"><img src='./images/scu_logo.png' align="center" style='vertical-align: middle; width: 22px;'></a>. I am also working as a research intern at [OPPO Research Institute](https://www.oppo.com/uk/) <a href='https://www.oppo.com/uk/' target="_blank"><img src='./images/oppo_logo.png' align="center" style='vertical-align: middle; width: 52px;'></a>, supervised by Prof. [Lei Zhang](https://www4.comp.polyu.edu.hk/~cslzhang/) ([PolyU](https://www.polyu.edu.hk/), IEEE Fellow). Previously, I have interned at [Ant Group](https://www.antgroup.com/en) <a href='https://www.antgroup.com/en' target="_blank"><img src='./images/alipay_logo.png' align="center" style='vertical-align: middle; width: 22px;'></a> focusing on GUI Agent, and [Taobao & Tmall Group](https://talent.taotian.com/) <a href='https://talent.taotian.com/' target="_blank"><img src='./images/taobao_logo.png' align="center" style='vertical-align: middle; width: 22px;'></a> working on Efficient VLMs. I've also spent half a year visiting [MiLAB](https://milab.westlake.edu.cn/) at [Westlake University](https://www.westlake.edu.cn/), supervised by Prof. [Donglin Wang](https://en.westlake.edu.cn/faculty/donglin-wang.html). I am fortunate to work closely with Dr. [Siteng Huang](https://kyonhuang.top/) from [DAMO Academy](https://damo.alibaba.com/) and Prof. [Linfeng Zhang](http://www.zhanglinfeng.tech/) from [SJTU](https://en.sjtu.edu.cn/).

📌 My research centers on **efficient Large Vision-Language Models (LVLMs)**, including:

- 🖼️ **Image-Text LVLMs**: high-resolution understanding via context compression and fast decoding, including [GlobalCom<sup>2</sup>](https://arxiv.org/abs/2501.05179), [FiCoCo](https://arxiv.org/abs/2411.17686), and [MixKV](https://arxiv.org/abs/2510.20707).
- 🎬 **Video Understanding**: long/audio-video, and streaming reasoning via efficient encoding and compression, including [VidCom<sup>2</sup>](https://arxiv.org/abs/2505.14454), [STC](https://arxiv.org/pdf/2512.00891), and [OmniSIFT](https://arxiv.org/abs/2602.04804).
- ⚙️ **Efficiency Toolbox**: efficient transfer/fine-tuning and benchmarking for downstream task adaptation, including [M2IST](https://arxiv.org/abs/2407.01131) and [V-PETL](https://openreview.net/forum?id=yS1dUkQFnu).

📢 If you find these directions interesting, feel free to reach out via email: `liuxuyang@stu.scu.edu.cn`.


## 🔥 News

<div class="news-scroll" markdown="1">

* **2026.01.26** 🎊🎊 Two papers have been accepted by **ICLR 2026**, including fast decoding for VLM/LLM via [MixKV](https://arxiv.org/abs/2510.20707) and the first safety study of dLLMs [DIJA](https://arxiv.org/abs/2507.11097)! Congratulations to all collaborators!
* **2025.12.02** 🤗🤗 We release [STC](https://arxiv.org/pdf/2512.00891), a plug-and-play inference acceleration framework for streaming video understanding! [Code](https://github.com/lern-to-write/STC) is available!
* **2025.11.08** 🎊🎊 Three papers have been accepted by **AAAI 2026**, including two LVLM acceleration methods [GlobalCom<sup>2</sup>](https://arxiv.org/abs/2501.05179) and [FiCoCo](https://arxiv.org/abs/2411.17686), and a RL-based GUI grounding training framework [GUI-G<sup>2</sup>](https://arxiv.org/abs/2507.15846)!
* **2025.08.21** 🎊🎊 One first author paper [VidCom<sup>2</sup>](https://arxiv.org/abs/2505.14454) about plug-and-play inference acceleration for VideoLLMs has been accepted by **EMNLP 2025** main conference! [Code](https://github.com/xuyang-liu16/VidCom2) is available!
* **2025.05.27** 🙌🙌 We release a new [paper](https://arxiv.org/abs/2505.19147), pointing to **shifting AI efficiency from model-centric to data-centric compression**. [Project](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression) is available! Our paper is honored to be the [#2 Paper of the day](https://huggingface.co/papers/2505.19147)!
* **2025.03.11** 🎊🎊 One first author paper ([M2IST](https://arxiv.org/abs/2407.01131)) about parameter-, memory-, and time-efficient fine-tuning for referring expression comprehension has been accepted by IEEE Transactions on Circuits and Systems for Video Technology (**TCSVT**)!
* **2025.02.22** 🎊🎊 Two papers ([ToCa](https://arxiv.org/abs/2410.05317) and [AutoGnothi](https://arxiv.org/abs/2410.21815)) have been accepted by **ICLR 2025**! Congratulations to all collaborators!
* **2024.09.26** 🎊🎊 One co-first author paper ([V-PETL](https://openreview.net/forum?id=yS1dUkQFnu)) about unified visual parameter-efficient transfer learning benchmark has been accepted by **NeurIPS 2024**!

</div>



## 📝 Publications 

Full publications are on my [Google Scholar](https://scholar.google.com/citations?user=9VhMC1QAAAAJ&hl=en) profile. *: Equal contribution. †: Project leader. <a href="https://scholar.google.com/citations?user=9VhMC1QAAAAJ" target="_blank"><img src="https://img.shields.io/badge/dynamic/json?label=Paper%20Citations&query=total_citations&url=https%3A%2F%2Fcse.bth.se%2F~fer%2Fgooglescholar-api%2Fgooglescholar.php%3Fuser%3D9VhMC1QAAAAJ&logo=googlescholar&style=social" alt="Google Scholar"></a> 

🚩 **Highlight:** ICLR: 4, NeurIPS: 1, AAAI: 3, EMNLP: 1.

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/MixKV_teaser.png' alt="MixKV teaser" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models**](https://openreview.net/forum?id=B2iqbCQviR)

<u>Xuyang Liu</u><sup>*</sup>, Xiyan Gui<sup>*</sup>, Yuchao Zhang, Linfeng Zhang

- Works with diverse LVLMs and LLMs, including LLaVA, Qwen-VL, InternVL, Llama, and Mistral series.
- Integrates with existing compressors (e.g., SnapKV, AdaKV, SparseMM) and consistently improves their performance.
- Delivers accuracy gains without sacrificing speed or memory efficiency.

<div style="display: inline">
  <a href="https://arxiv.org/pdf/2510.20707"><strong>[paper]</strong></a>
  <a href="https://github.com/xuyang-liu16/MixKV"><strong>[code]</strong></a>
</div>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025</div><img src='images/VidCom2_teaser.png' alt="VidCom2 teaser" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models**](https://aclanthology.org/2025.emnlp-main.98/)

<u>Xuyang Liu</u><sup>*</sup>, Yiyu Wang<sup>*</sup>, Junpeng Ma, Linfeng Zhang

- Compatible with major VideoLLMs, including LLaVA, Qwen-VL, and Qwen-Omni series.
- Uses only 25% of tokens while preserving 99.6% performance of LLaVA-OV.
- Reduces LLaVA-OV generation time by 70.8% and overall latency by 43.0%.

<div style="display: inline">
  <a href="https://arxiv.org/pdf/2505.14454"><strong>[paper]</strong></a>
  <a href="https://github.com/xuyang-liu16/VidCom2"><strong>[code]</strong></a>
  <a href="http://xhslink.com/o/7SMiHSgXFFU"><strong>[Xiaohongshu]</strong></a>
  <a href="https://www.jiqizhixin.com/articles/2025-12-15-6"><strong>[机器之心]</strong></a>
  <a href="https://mp.weixin.qq.com/s/hQhEPlBWd4noVGSOWT4_XQ"><strong>[PaperWeekly]</strong></a>
  <a href="/files/EMNLP-2025-main-262.pdf"><strong>[slides]</strong></a>
  <a href="/files/EMNLP-2025-main-262-Poster.pdf"><strong>[poster]</strong></a>
  <a href="https://underline.io/events/502/posters/20833/poster/129850-video-compression-commander-plug-and-play-inference-acceleration-for-video-large-language-models"><strong>[video]</strong></a>
</div>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='images/GlobalCom2_teaser.png' alt="GlobalCom2 teaser" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[**Global Compression Commander: Plug-and-Play Inference Acceleration for High-Resolution Large Vision-Language Models**](https://arxiv.org/abs/2501.05179)

<u>Xuyang Liu</u>, Ziming Wang, Junjie Chen, Yuhang Han, Yingyao Wang, Jiale Yuan, Jun Song, Siteng Huang, Honggang Chen

- Compatible with major HR-LVLMs, including LLaVA-NeXT and LLaVA-OV.
- Uses only 10% of tokens while maintaining above 90% performance across 10 tasks.
- Reduces FLOPs and peak memory to 9.1% and 60%, and achieves 1.8x throughput.

<div style="display: inline">
  <a href="https://arxiv.org/pdf/2501.05179"><strong>[paper]</strong></a>
  <a href="https://github.com/xuyang-liu16/GlobalCom2"><strong>[code]</strong></a>
  <a href="/files/AAAI-2026-GlobalCom2-Poster.pdf"><strong>[poster]</strong></a>
</div>

</div>
</div>

### Conference Papers

<a href="https://openreview.net/forum?id=B2iqbCQviR" target="_blank"><img src="https://img.shields.io/badge/ICLR-2026-blue?style=flat-square"></a> <u>Xuyang Liu</u><sup>\*</sup>, Xiyan Gui<sup>\*</sup>, Yuchao Zhang, Linfeng Zhang, &quot;**Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models**&quot;. In *International Conference on Learning Representations (ICLR)*, 2026. [[paper](https://arxiv.org/pdf/2510.20707)] [[code](https://github.com/xuyang-liu16/MixKV)] <a href="https://github.com/xuyang-liu16/MixKV" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/MixKV?style=social"></a>

<a href="https://openreview.net/forum?id=rIPeatvPy3" target="_blank"><img src="https://img.shields.io/badge/ICLR-2026-blue?style=flat-square"></a> Zichen Wen, Jiashu Qu, Dongrui Liu, Zhiyuan Liu, Ruixi Wu, Yicun Yang, Xiangqi Jin, Haoyun Xu, <u>Xuyang Liu</u>, Weijia Li, Chaochao Lu, Jing Shao, Conghui He, Linfeng Zhang, &quot;**The Devil behind the mask: An emergent safety vulnerability of Diffusion LLMs**&quot;. In *International Conference on Learning Representations (ICLR)*, 2026. [[paper](https://arxiv.org/pdf/2507.11097)] [[code](https://github.com/ZichenWen1/DIJA)] [[huggingface paper](https://huggingface.co/papers/2507.11097)] [[量子位](https://mp.weixin.qq.com/s/nfyZFXN7ku07_9tTzG-W9Q)] <a href="https://github.com/ZichenWen1/DIJA" target="_blank"><img src="https://img.shields.io/github/stars/ZichenWen1/DIJA?style=social"></a> 

<a href="https://arxiv.org/abs/2501.05179" target="_blank"><img src="https://img.shields.io/badge/AAAI-2026-blue?style=flat-square"></a> <u>Xuyang Liu</u>, Ziming Wang, Junjie Chen, Yuhang Han, Yingyao Wang, Jiale Yuan, Jun Song, Siteng Huang, Honggang Chen, &quot;**Global Compression Commander: Plug-and-Play Inference Acceleration for High-Resolution Large Vision-Language Models**&quot;. In *Proceedings of the 40th AAAI Conference on Artificial Intelligence*, 2026. [[paper](https://arxiv.org/pdf/2501.05179)] [[code](https://github.com/xuyang-liu16/GlobalCom2)] [[poster](/files/AAAI-2026-GlobalCom2-Poster.pdf)] <a href="https://github.com/xuyang-liu16/GlobalCom2" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/GlobalCom2?style=social"></a>

<a href="https://arxiv.org/abs/2411.17686" target="_blank"><img src="https://img.shields.io/badge/AAAI-2026-blue?style=flat-square"></a> Yuhang Han<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Zihan Zhang, Pengxiang Ding, Junjie Chen, Donglin Wang, Honggang Chen, Qingsen Yan, Siteng Huang, &quot;**Filter, Correlate, Compress: Training-Free Token Reduction for MLLM Acceleration**&quot;. In *Proceedings of the 40th AAAI Conference on Artificial Intelligence*, 2026. [[paper](https://arxiv.org/pdf/2411.17686)] [[page](https://ficoco-accelerate.github.io/)] [[code](https://github.com/kawhiiiileo/FiCoCo)][[poster](/files/AAAI-2026-Poster-FiCoCo.pdf)] <a href="https://github.com/kawhiiiileo/FiCoCo" target="_blank"><img src="https://img.shields.io/github/stars/kawhiiiileo/FiCoCo?style=social"></a>

<a href="https://arxiv.org/abs/2507.15846" target="_blank"><img src="https://img.shields.io/badge/AAAI-2026-blue?style=flat-square"></a> Fei Tang, Zhangxuan Gu, Zhengxi Lu, <u>Xuyang Liu</u>, Shuheng Shen, Changhua Meng, Wen Wang, Wenqi Zhang, Yongliang Shen, Weiming Lu, Jun Xiao, Yueting Zhuang, &quot;**GUI-G<sup>2</sup>: Gaussian Reward Modeling for GUI Grounding**&quot;. In *Proceedings of the 40th AAAI Conference on Artificial Intelligence*, 2026. [[paper](https://arxiv.org/pdf/2507.15846)] [[code](https://github.com/zju-real/GUI-G2)] [[huggingface paper](https://huggingface.co/papers/2507.15846)] [[page](https://zju-real.github.io/GUI-G2)] [[机器之心](https://mp.weixin.qq.com/s/DRMtB-o9X_CzEFGkxw0Ycw)] <a href="https://github.com/zju-real/GUI-G2" target="_blank"><img src="https://img.shields.io/github/stars/zju-real/GUI-G2?style=social"></a>

<a href="https://aclanthology.org/2025.emnlp-main.98/" target="_blank"><img src="https://img.shields.io/badge/EMNLP-2025-blue?style=flat-square"></a> <u>Xuyang Liu</u><sup>\*</sup>, Yiyu Wang<sup>\*</sup>, Junpeng Ma, Linfeng Zhang, &quot;**Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models**&quot;. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2025. [[paper](https://arxiv.org/pdf/2505.14454)] [[code](https://github.com/xuyang-liu16/VidCom2)] [[Xiaohongshu](http://xhslink.com/o/7SMiHSgXFFU )] [[机器之心](https://www.jiqizhixin.com/articles/2025-12-15-6)] [[PaperWeekly](https://mp.weixin.qq.com/s/hQhEPlBWd4noVGSOWT4_XQ)] [[slides](/files/EMNLP-2025-main-262.pdf)] [[poster](/files/EMNLP-2025-main-262-Poster.pdf)] [[video](https://underline.io/events/502/posters/20833/poster/129850-video-compression-commander-plug-and-play-inference-acceleration-for-video-large-language-models)] <a href="https://github.com/xuyang-liu16/VidCom2" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/VidCom2?style=social"></a>

<a href="https://openreview.net/forum?id=yYZbZGo4ei" target="_blank"><img src="https://img.shields.io/badge/ICLR-2025-blue?style=flat-square"></a> Chang Zou<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Ting Liu, Siteng Huang, Linfeng Zhang, &quot;**Accelerating Diffusion Transformers with Token-wise Feature Caching**&quot;. In *International Conference on Learning Representations (ICLR)*, 2025. [[paper](https://arxiv.org/pdf/2410.05317)] [[page](https://toca2024.github.io/ToCa/)] [[code](https://github.com/Shenyi-Z/ToCa)] [[量子位](https://mp.weixin.qq.com/s/ZqVWslSEdjX00VMf6RqtcA)] [[poster](/files/ICLR-2025-ToCa-Poster.pdf)] <a href="https://github.com/Shenyi-Z/ToCa" target="_blank"><img src="https://img.shields.io/github/stars/Shenyi-Z/ToCa?style=social"></a>

<a href="https://openreview.net/forum?id=UvMSKonce8" target="_blank"><img src="https://img.shields.io/badge/ICLR-2025-blue?style=flat-square"></a> Shaobo Wang, Hongxuan Tang, Mingyang Wang, Hongrui Zhang, <u>Xuyang Liu</u>, Weiya Li, Xuming Hu, Linfeng Zhang, &quot;**Gnothi Seauton: Empowering Faithful Self-Interpretability in Black-Box Models**&quot;. In *International Conference on Learning Representations (ICLR)*, 2025. [[paper](https://arxiv.org/pdf/2410.21815)] [[code](https://github.com/gszfwsb/AutoGnothi)] <a href="https://github.com/gszfwsb/AutoGnothi" target="_blank"><img src="https://img.shields.io/github/stars/gszfwsb/AutoGnothi?style=social"></a>

<a href="https://openreview.net/forum?id=yS1dUkQFnu" target="_blank"><img src="https://img.shields.io/badge/NeurIPS-2024-blue?style=flat-square"></a> Yi Xin<sup>\*</sup>, Siqi Luo<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Yuntao Du<sup>\*</sup>, Haodi Zhou, Xinyu Cheng, Christina Lee, and 10 more authors, &quot;**V-PETL Bench: A Unified Visual Parameter-Efficient Transfer Learning Benchmark**&quot;. In *Neural Information Processing Systems Datasets and Benchmarks Track (NeurlPS D&B Track)*, 2024. [[paper](https://openreview.net/forum?id=yS1dUkQFnu)][[page](https://v-petl-bench.github.io/)] [[code](https://github.com/synbol/Parameter-Efficient-Transfer-Learning-Benchmark)] [[poster](https://neurips.cc/virtual/2024/poster/97434)] <a href="https://github.com/synbol/Parameter-Efficient-Transfer-Learning-Benchmark" target="_blank"><img src="https://img.shields.io/github/stars/synbol/Parameter-Efficient-Transfer-Learning-Benchmark?style=social"></a>

<!--
<a href="https://ieeexplore.ieee.org/document/10445945" target="_blank"><img src="https://img.shields.io/badge/ICASSP-2024-blue?style=flat-square"></a> <u>Xuyang Liu</u><sup>\*</sup>, Siteng Huang<sup>\*</sup>, Yachen Kang, Honggang Chen, Donglin Wang, &quot;**VGDiffZero: Text-to-image Diffusion Models Can Be Zero-shot Visual Grounders**&quot;. In *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)*, 2024. [[paper](https://arxiv.org/pdf/2309.01141.pdf)] [[code](https://github.com/xuyang-liu16/VGDiffZero)] [[poster](/files/ICASSP-2024-VGDiffZero-Poster.pdf)] <a href="https://github.com/xuyang-liu16/VGDiffZero" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/VGDiffZero?style=social"></a>

<a href="https://ieeexplore.ieee.org/document/10688132" target="_blank"><img src="https://img.shields.io/badge/ICME-2024-blue?style=flat-square"></a> Ting Liu<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Siteng Huang, Honggang Chen, Quanjun Yin, Long Qin, Donglin Wang, Yue Hu, &quot;**DARA: Domain- and Relation-aware Adapters Make Parameter-efficient Tuning for Visual Grounding**&quot;. In *IEEE International Conference on Multimedia & Expo (ICME)*, 2024. (<span style="color: red">**Oral**</span>) [[paper](https://arxiv.org/pdf/2405.06217)] [[code](https://github.com/liuting20/DARA)] [[poster](/files/ICME-2024-DARA-Poster.pdf)] <a href="https://github.com/liuting20/DARA" target="_blank"><img src="https://img.shields.io/github/stars/liuting20/DARA?style=social"></a> 
-->


### Journal Papers

<a href="https://ieeexplore.ieee.org/document/10929057" target="_blank"><img src="https://img.shields.io/badge/TCSVT-2025-54b345?style=flat-square"></a> <u>Xuyang Liu</u><sup>\*</sup>, Ting Liu<sup>\*</sup>, Siteng Huang, Yi Xin, Yue Hu, Quanjun Yin, Donglin Wang, Yuanyuan Wu, Honggang Chen, &quot;**M2IST: Multi-Modal Interactive Side-Tuning for Efficient Referring Expression Comprehension**&quot;. *IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)*, 2025. [[paper](https://arxiv.org/pdf/2407.01131)] [[code](https://github.com/xuyang-liu16/M2IST)]

<!-- 
<a href="https://ieeexplore.ieee.org/document/11206397" target="_blank"><img src="https://img.shields.io/badge/TCSS-2025-54b345?style=flat-square"></a> Junjie Chen, <u>Xuyang Liu</u>, Subin Huang, Linfeng Zhang, Hang Yu &quot;**Seeing Sarcasm Through Different Eyes: Analyzing Multimodal Sarcasm Perception in Large Vision-Language Models**&quot;. *IEEE Transactions on Computational Social Systems (TCSS)*, 2025. [[paper](https://arxiv.org/pdf/2503.12149)] [[code](https://github.com/CoderChen01/LVLMSarcasmAnalysis)] 

<a href="https://ieeexplore.ieee.org/document/10742110" target="_blank"><img src="https://img.shields.io/badge/TBC-2024-54b345?style=flat-square"></a> Xinying Lin, <u>Xuyang Liu</u>, Hong Yang, Xiaohai He, Honggang Chen, &quot;**Perception- and Fidelity-aware Reduced-Reference Super-Resolution Image Quality Assessment**&quot;. *IEEE Transactions on Broadcasting (TBC)*, 2024. [[paper](https://arxiv.org/pdf/2405.09472)] [[code](https://github.com/xinyouu/PFIQA)] 

<a href="https://www.sciencedirect.com/science/article/abs/pii/S0140366422002535" target="_blank"><img src="https://img.shields.io/badge/COMPUT COMMUN-2022-54b345?style=flat-square"></a> <u>Xuyang Liu</u>, &quot;**GLMLP-TRANS: A transportation mode detection model using lightweight sensors integrated in smartphones**&quot;. *Computer Communications*, 2022. [[paper](https://www.sciencedirect.com/science/article/abs/pii/S0140366422002535)] [[code](https://github.com/xuyang-liu16/GLMLP-TRANS)] 
-->


### Preprints & Under Submission

<a href="https://arxiv.org/abs/2602.04804" target="_blank"><img src="https://img.shields.io/badge/arXiv-2602.04804-B31B1B?style=flat-square"></a> Yue Ding, Yiyan Ji, Jungang Li, <u>Xuyang Liu</u>, Xinlong Chen, and 10 more authors, &quot;**OmniSIFT: Modality-Asymmetric Token Compression for Efficient Omni-modal Large Language Models**&quot;. *arXiv preprint arXiv:2602.04804*. [[paper](https://arxiv.org/pdf/2602.04804)] [[huggingface paper](https://huggingface.co/papers/2602.04804)]

<a href="https://arxiv.org/abs/2512.00891" target="_blank"><img src="https://img.shields.io/badge/arXiv-2512.00891-B31B1B?style=flat-square"></a> Yiyu Wang<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*,†</sup>, Xiyan Gui, Xinying Lin, Boxue Yang, Chenfei Liao, Tailai Chen, Linfeng Zhang, &quot;**Accelerating Streaming Video Large Language Models via Hierarchical Token Compression**&quot;. *arXiv preprint arXiv:2512.00891*. [[paper](https://arxiv.org/pdf/2512.00891)] [[code](https://github.com/lern-to-write/STC)] [[PaperWeekly](https://mp.weixin.qq.com/s/PsNkR28yIFXqAQmAb62Yrg
)] <a href="https://github.com/lern-to-write/STC" target="_blank"><img src="https://img.shields.io/github/stars/lern-to-write/STC?style=social"></a>

<!-- 
<a href="https://arxiv.org/abs/2510.14359" target="_blank"><img src="https://img.shields.io/badge/arXiv-2510.14359-B31B1B?style=flat-square"></a> Zichen Wen, Yiyu Wang, Chenfei Liao, Boxue Yang, Junxian Li, Weifeng Liu, Haocong He, Bolong Feng, <u>Xuyang Liu</u>, Yuanhuiyi Lyu, Xu Zheng, Xuming Hu, Linfeng Zhang &quot;**AI for Service: Proactive Assistance with AI Glasses**&quot;. *arXiv preprint arXiv:2510.14359*. [[paper](https://arxiv.org/pdf/2510.14359)] [[huggingface paper](https://huggingface.co/papers/2510.14359)]
-->

<a href="https://arxiv.org/abs/2509.01552" target="_blank"><img src="https://img.shields.io/badge/arXiv-2509.01552-B31B1B?style=flat-square"></a> Junjie Chen<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*,†</sup>, Zichen Wen, Yiyu Wang, Siteng Huang, Honggang Chen, &quot;**Variation-aware Vision Token Dropping for Faster Large Vision-Language Models**&quot;. *arXiv preprint arXiv:2509.01552*. [[paper](https://arxiv.org/pdf/2509.01552)] [[code](https://github.com/xuyang-liu16/V2Drop)]

<!-- 
<a href="https://arxiv.org/abs/2508.13305" target="_blank"><img src="https://img.shields.io/badge/arXiv-2508.13305-B31B1B?style=flat-square"></a> Minhao Xiong, Zichen Wen, Zhuangcheng Gu, <u>Xuyang Liu</u>, Rui Zhang, Hengrui Kang, Jiabing Yang, Junyuan Zhang, Weijia Li, Conghui He, Yafei Wang, Linfeng Zhang, &quot;**Prune2Drive: A Plug-and-Play Framework for Accelerating Vision-Language Models in Autonomous Driving**&quot;. *arXiv preprint arXiv:2508.13305*. [[paper](https://arxiv.org/pdf/2508.13305)] 
-->


<a href="https://arxiv.org/abs/2505.19147" target="_blank"><img src="https://img.shields.io/badge/arXiv-2505.19147-B31B1B?style=flat-square"></a> <u>Xuyang Liu</u><sup>\*</sup>, Zichen Wen<sup>\*</sup>, Shaobo Wang<sup>\*</sup>, Junjie Chen, Zhishan Tao, and 10 more authors, &quot;**Shifting AI Efficiency From Model-Centric to Data-Centric Compression**&quot;. *arXiv preprint arXiv:2505.19147*. [[paper](https://arxiv.org/pdf/2505.19147)] [[project](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression)] [[huggingface paper](https://huggingface.co/papers/2505.19147)] [[Twitter@Rohan Paul](https://x.com/rohanpaul_ai/status/1936896115078525067?s=20)] <a href="https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/Awesome-Token-level-Model-Compression?style=social"></a> 

<a href="https://arxiv.org/abs/2405.14700" target="_blank"><img src="https://img.shields.io/badge/arXiv-2405.14700-B31B1B?style=flat-square"></a> Ting Liu<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Liangtao Shi, Zunnan Xu, Yue Hu, Siteng Huang, Yi Xin, Bineng Zhong, Donglin Wang, &quot;**Sparse-Tuning: Adapting Vision Transformers with Efficient Fine-tuning and Inference**&quot;. *arXiv preprint arXiv:2405.14700*. [[paper](https://arxiv.org/pdf/2405.14700)] [[github](https://github.com/liuting20/Sparse-Tuning)] <a href="https://github.com/liuting20/Sparse-Tuning" target="_blank"><img src="https://img.shields.io/github/stars/liuting20/Sparse-Tuning?style=social"></a>


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
* IEEE Transactions on Circuits and Systems for Video Technology ([TCSVT](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=76))
* Computer Vision and Image Understanding ([CVIU](https://www.sciencedirect.com/journal/computer-vision-and-image-understanding))
