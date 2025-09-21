---
permalink: /
title: "Xuyang Liu (刘旭洋)"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---


🌈 I am a third-year Master's student at [Sichuan University](https://en.scu.edu.cn/). I am also working as a research intern at OPPO Research Institute, supervised by Prof. [Lei Zhang](https://www4.comp.polyu.edu.hk/~cslzhang/) (PolyU HK, IEEE Fellow). Previously, I have interned at [Ant Security Lab](https://securitylab.antgroup.com/home) focusing on GUI Agent, and [Taobao & Tmall Group](https://talent.taotian.com/) working on Efficient MLLM. I've also spent half a year visiting [MiLAB](https://milab.westlake.edu.cn/) at Westlake University, supervised by Prof. [Donglin Wang](https://en.westlake.edu.cn/faculty/donglin-wang.html). I am fortunate to work closely with Dr. [Siteng Huang](https://kyonhuang.top/) from DAMO Academy and Prof. [Linfeng Zhang](http://www.zhanglinfeng.tech/) from SJTU.

<!-- 📌 My research interests span **Efficient Multi-modal Large Language Models**, including:

* **Discrimination**: [visual grounding](https://github.com/linhuixiao/Awesome-Visual-Grounding) and [referring video object segmentation](https://github.com/gaomingqi/Awesome-Video-Object-Segmentation).
* **Adaptation**: [parameter-efficient transfer learning](https://github.com/synbol/Awesome-Parameter-Efficient-Transfer-Learning) and [model compression](https://github.com/MingSun-Tse/Efficient-Deep-Learning).  
* **Reconstruction**: [super-resolution](https://github.com/ChaofWang/Awesome-Super-Resolution) and [image quality assessment](https://github.com/chaofengc/Awesome-Image-Quality-Assessment).
* **Generation**: [text-to-image generation](https://github.com/AlonzoLeeeooo/awesome-text-to-image-studies) and [text-to-video generation](https://github.com/soraw-ai/Awesome-Text-to-Video-Generation). -->

📌 My research interests span **Efficient Vision-Language Models**, including:
* **Efficient Inference**: [V<sup>2</sup>Drop](https://arxiv.org/abs/2509.01552), [VidCom<sup>2</sup>](https://arxiv.org/abs/2505.14454), [GlobalCom<sup>2</sup>](https://arxiv.org/abs/2501.05179), [FiCoCo](https://arxiv.org/abs/2411.17686), [ToCa](https://arxiv.org/abs/2410.05317), [Sparse-Tuning](https://arxiv.org/abs/2405.14700)
* **Efficient Training**: [M2IST](https://arxiv.org/abs/2407.01131), [V-PETL Bench](https://openreview.net/forum?id=yS1dUkQFnu), [DARA](https://arxiv.org/abs/2405.06217), [Sparse-Tuning](https://arxiv.org/abs/2405.14700), [AutoGnothi](https://arxiv.org/abs/2410.21815)

📢 Recently, I am mainly focusing on **[Token-level Model Compression](https://arxiv.org/abs/2505.19147)**, and applying it to efficient **long video understanding**. Feel free to reach out to me via Email `liuxuyang@stu.scu.edu.cn`, if you are interested in collaborating with me.


## 🔥 News

* **2025.05.27** 🙌🙌 We release a new [paper](https://arxiv.org/abs/2505.19147), pointing to **shifting AI efficiency from model-centric to data-centric compression**. [Project](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression) is available! Our paper is honored to be the [#2 Paper of the day](https://huggingface.co/papers/2505.19147)!
* **2025.03.11** 🎊🎊 One first author paper ([M2IST](https://arxiv.org/abs/2407.01131)) about parameter-, memory-, and time-efficient fine-tuning for referring expression comprehension has been accepted by IEEE Transactions on Circuits and Systems for Video Technology (**TCSVT**)!
* **2025.02.22**: 🎊🎊 Two papers ([ToCa](https://arxiv.org/abs/2410.05317) and [AutoGnothi](https://arxiv.org/abs/2410.21815)) have been accepted by **ICLR 2025**! Congratulations to all collaborators!
* **2025.01.10**: 🤗🤗 We release [GlobalCom<sup>2</sup>](https://arxiv.org/abs/2501.05179), a "global-to-local" approach for training-free acceleration of **high-resolution LVLMs** with dynamic tiling strategy. [Code](https://github.com/xuyang-liu16/GlobalCom2) is available!
* **2024.09.26**: 🎊🎊 One co-first author paper ([V-PETL](https://openreview.net/forum?id=yS1dUkQFnu)) about unified visual parameter-efficient transfer learning benchmark has been accepted by **NeurIPS 2024**!



## 📝 Publications 

Please find my full publications on my [Google Scholar](https://scholar.google.com/citations?user=9VhMC1QAAAAJ&hl=en) profile.   <a href="https://scholar.google.com/citations?user=9VhMC1QAAAAJ" target="_blank"><img src="https://img.shields.io/badge/dynamic/json?label=Paper%20Citations&query=total_citations&url=https%3A%2F%2Fcse.bth.se%2F~fer%2Fgooglescholar-api%2Fgooglescholar.php%3Fuser%3D9VhMC1QAAAAJ&logo=googlescholar&style=social" alt="Google Scholar"></a> 

### Conference Papers

<a href="https://openreview.net/forum?id=yYZbZGo4ei" target="_blank"><img src="https://img.shields.io/badge/ICLR-2025-blue?style=flat-square"></a> Chang Zou<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Ting Liu, Siteng Huang, Linfeng Zhang, &quot;**Accelerating Diffusion Transformers with Token-wise Feature Caching**&quot;. In *International Conference on Learning Representations (ICLR)*, 2025. [[paper](https://arxiv.org/pdf/2410.05317)] [[page](https://toca2024.github.io/ToCa/)] [[code](https://github.com/Shenyi-Z/ToCa)] [[量子位](https://mp.weixin.qq.com/s/ZqVWslSEdjX00VMf6RqtcA)] [[poster](/files/ICLR-2025-ToCa-Poster.pdf)] <a href="https://github.com/Shenyi-Z/ToCa" target="_blank"><img src="https://img.shields.io/github/stars/Shenyi-Z/ToCa?style=social"></a>

<a href="https://openreview.net/forum?id=UvMSKonce8" target="_blank"><img src="https://img.shields.io/badge/ICLR-2025-blue?style=flat-square"></a> Shaobo Wang, Hongxuan Tang, Mingyang Wang, Hongrui Zhang, <u>Xuyang Liu</u>, Weiya Li, Xuming Hu, Linfeng Zhang, &quot;**Gnothi Seauton: Empowering Faithful Self-Interpretability in Black-Box Models**&quot;. In *International Conference on Learning Representations (ICLR)*, 2025. [[paper](https://arxiv.org/pdf/2410.21815)] [[code](https://github.com/gszfwsb/AutoGnothi)] <a href="https://github.com/gszfwsb/AutoGnothi" target="_blank"><img src="https://img.shields.io/github/stars/gszfwsb/AutoGnothi?style=social"></a>

<a href="https://openreview.net/forum?id=yS1dUkQFnu" target="_blank"><img src="https://img.shields.io/badge/NeurIPS-2024-blue?style=flat-square"></a> Yi Xin<sup>\*</sup>, Siqi Luo<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Yuntao Du<sup>\*</sup>, Haodi Zhou, Xinyu Cheng, Christina Lee, and 10 more authors, &quot;**V-PETL Bench: A Unified Visual Parameter-Efficient Transfer Learning Benchmark**&quot;. In *Neural Information Processing Systems Datasets and Benchmarks Track (NeurlPS D&B Track)*, 2024. [[paper](https://openreview.net/forum?id=yS1dUkQFnu)][[page](https://v-petl-bench.github.io/)] [[code](https://github.com/synbol/Parameter-Efficient-Transfer-Learning-Benchmark)] [[poster](https://neurips.cc/virtual/2024/poster/97434)] <a href="https://github.com/synbol/Parameter-Efficient-Transfer-Learning-Benchmark" target="_blank"><img src="https://img.shields.io/github/stars/synbol/Parameter-Efficient-Transfer-Learning-Benchmark?style=social"></a>

<a href="https://ieeexplore.ieee.org/document/10445945" target="_blank"><img src="https://img.shields.io/badge/ICASSP-2024-blue?style=flat-square"></a> <u>Xuyang Liu</u><sup>\*</sup>, Siteng Huang<sup>\*</sup>, Yachen Kang, Honggang Chen, Donglin Wang, &quot;**VGDiffZero: Text-to-image Diffusion Models Can Be Zero-shot Visual Grounders**&quot;. In *IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)*, 2024. [[paper](https://arxiv.org/pdf/2309.01141.pdf)] [[code](https://github.com/xuyang-liu16/VGDiffZero)] [[poster](/files/ICASSP-2024-VGDiffZero-Poster.pdf)] <a href="https://github.com/xuyang-liu16/VGDiffZero" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/VGDiffZero?style=social"></a> 

<a href="https://ieeexplore.ieee.org/document/10688132" target="_blank"><img src="https://img.shields.io/badge/ICME-2024-blue?style=flat-square"></a> Ting Liu<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Siteng Huang, Honggang Chen, Quanjun Yin, Long Qin, Donglin Wang, Yue Hu, &quot;**DARA: Domain- and Relation-aware Adapters Make Parameter-efficient Tuning for Visual Grounding**&quot;. In *IEEE International Conference on Multimedia & Expo (ICME)*, 2024. (<span style="color: red">**Oral**</span>) [[paper](https://arxiv.org/pdf/2405.06217)] [[code](https://github.com/liuting20/DARA)] [[poster](/files/ICME-2024-DARA-Poster.pdf)] <a href="https://github.com/liuting20/DARA" target="_blank"><img src="https://img.shields.io/github/stars/liuting20/DARA?style=social"></a>


### Journal Papers

<a href="https://ieeexplore.ieee.org/document/10929057" target="_blank"><img src="https://img.shields.io/badge/TCSVT-2025-54b345?style=flat-square"></a> <u>Xuyang Liu</u><sup>\*</sup>, Ting Liu<sup>\*</sup>, Siteng Huang, Yi Xin, Yue Hu, Quanjun Yin, Donglin Wang, Yuanyuan Wu, Honggang Chen &quot;**M2IST: Multi-Modal Interactive Side-Tuning for Efficient Referring Expression Comprehension**&quot;. *IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)*, 2025. [[paper](https://arxiv.org/pdf/2407.01131)] [[code](https://github.com/xuyang-liu16/M2IST)]

<a href="https://arxiv.org/abs/2503.12149" target="_blank"><img src="https://img.shields.io/badge/TCSS-2025-54b345?style=flat-square"></a> Junjie Chen, <u>Xuyang Liu</u>, Subin Huang, Linfeng Zhang, Hang Yu &quot;**Seeing Sarcasm Through Different Eyes: Analyzing Multimodal Sarcasm Perception in Large Vision-Language Models**&quot;. *IEEE Transactions on Computational Social Systems (TCSS)*, 2025. [[paper](https://arxiv.org/pdf/2503.12149)] [[code](https://github.com/CoderChen01/LVLMSarcasmAnalysis)] 

<a href="https://ieeexplore.ieee.org/document/10742110" target="_blank"><img src="https://img.shields.io/badge/TBC-2024-54b345?style=flat-square"></a> Xinying Lin, <u>Xuyang Liu</u>, Hong Yang, Xiaohai He, Honggang Chen, &quot;**Perception- and Fidelity-aware Reduced-Reference Super-Resolution Image Quality Assessment**&quot;. *IEEE Transactions on Broadcasting (TBC)*, 2024. [[paper](https://arxiv.org/pdf/2405.09472)] [[code](https://github.com/xinyouu/PFIQA)] 

<a href="https://www.sciencedirect.com/science/article/abs/pii/S0140366422002535" target="_blank"><img src="https://img.shields.io/badge/COMPUT COMMUN-2022-54b345?style=flat-square"></a> <u>Xuyang Liu</u>, &quot;**GLMLP-TRANS: A transportation mode detection model using lightweight sensors integrated in smartphones**&quot;. *Computer Communications*, 2022. [[paper](https://www.sciencedirect.com/science/article/abs/pii/S0140366422002535)] [[code](https://github.com/xuyang-liu16/GLMLP-TRANS)] 


### Preprints & Under Submission

<a href="https://arxiv.org/abs/2509.01552" target="_blank"><img src="https://img.shields.io/badge/arXiv-2509.01552-B31B1B?style=flat-square"></a> Junjie Chen<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*,†</sup>, Zichen Wen, Yiyu Wang, Siteng Huang, Honggang Chen &quot;**Variation-aware Vision Token Dropping for Faster Large Vision-Language Models**&quot;. *arXiv preprint arXiv:2509.01552*. [[paper](https://arxiv.org/pdf/2509.01552)] [[code](https://github.com/xuyang-liu16/V2Drop)]

<a href="https://arxiv.org/abs/2508.13305" target="_blank"><img src="https://img.shields.io/badge/arXiv-2508.13305-B31B1B?style=flat-square"></a> Minhao Xiong, Zichen Wen, Zhuangcheng Gu, <u>Xuyang Liu</u>, Rui Zhang, Hengrui Kang, Jiabing Yang, Junyuan Zhang, Weijia Li, Conghui He, Yafei Wang, Linfeng Zhang, &quot;**Prune2Drive: A Plug-and-Play Framework for Accelerating Vision-Language Models in Autonomous Driving**&quot;. *arXiv preprint arXiv:2508.13305*. [[paper](https://arxiv.org/pdf/2508.13305)] 

<a href="https://arxiv.org/abs/2507.15846" target="_blank"><img src="https://img.shields.io/badge/arXiv-2507.15846-B31B1B?style=flat-square"></a> Fei Tang, Zhangxuan Gu, Zhengxi Lu, <u>Xuyang Liu</u>, Shuheng Shen, Changhua Meng, Wen Wang, Wenqi Zhang, Yongliang Shen, Weiming Lu, Jun Xiao, Yueting Zhuang, &quot;**GUI-G<sup>2</sup>: Gaussian Reward Modeling for GUI Grounding**&quot;. *arXiv preprint arXiv:2507.15846*. [[paper](https://arxiv.org/pdf/2507.15846)] [[code](https://github.com/zju-real/GUI-G2)] [[huggingface paper](https://huggingface.co/papers/2507.15846)] [[page](https://zju-real.github.io/GUI-G2)] [[机器之心](https://mp.weixin.qq.com/s/DRMtB-o9X_CzEFGkxw0Ycw)] <a href="https://github.com/zju-real/GUI-G2" target="_blank"><img src="https://img.shields.io/github/stars/zju-real/GUI-G2?style=social"></a> 

<a href="https://arxiv.org/abs/2507.11097" target="_blank"><img src="https://img.shields.io/badge/arXiv-2507.11097-B31B1B?style=flat-square"></a> Zichen Wen, Jiashu Qu, Dongrui Liu, Zhiyuan Liu, Ruixi Wu, Yicun Yang, Xiangqi Jin, Haoyun Xu, <u>Xuyang Liu</u>, Weijia Li, Chaochao Lu, Jing Shao, Conghui He, Linfeng Zhang, &quot;**The Devil behind the mask: An emergent safety vulnerability of Diffusion LLMs**&quot;. *arXiv preprint arXiv:2507.11097*. [[paper](https://arxiv.org/pdf/2507.11097)] [[code](https://github.com/ZichenWen1/DIJA)] [[huggingface paper](https://huggingface.co/papers/2507.11097)] [[量子位](https://mp.weixin.qq.com/s/nfyZFXN7ku07_9tTzG-W9Q)] <a href="https://github.com/ZichenWen1/DIJA" target="_blank"><img src="https://img.shields.io/github/stars/ZichenWen1/DIJA?style=social"></a> 

<a href="https://arxiv.org/abs/2505.19147" target="_blank"><img src="https://img.shields.io/badge/arXiv-2505.19147-B31B1B?style=flat-square"></a> <u>Xuyang Liu</u><sup>\*</sup>, Zichen Wen<sup>\*</sup>, Shaobo Wang<sup>\*</sup>, Junjie Chen, Zhishan Tao, and 10 more authors, &quot;**Shifting AI Efficiency From Model-Centric to Data-Centric Compression**&quot;. *arXiv preprint arXiv:2505.19147*. [[paper](https://arxiv.org/pdf/2505.19147)] [[project](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression)] [[huggingface paper](https://huggingface.co/papers/2505.19147)] [[video](https://www.youtube.com/watch?v=qT8k5-DVdcU)]<a href="https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/Awesome-Token-level-Model-Compression?style=social"></a> 

<a href="https://arxiv.org/abs/2505.14454" target="_blank"><img src="https://img.shields.io/badge/arXiv-2505.14454-B31B1B?style=flat-square"></a> <u>Xuyang Liu</u><sup>\*</sup>, Yiyu Wang<sup>\*</sup>, Junpeng Ma, Linfeng Zhang, &quot;**Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models**&quot;. *arXiv preprint arXiv:2505.14454*. [[paper](https://arxiv.org/pdf/2505.14454)] [[code](https://github.com/xuyang-liu16/VidCom2)] <a href="https://github.com/xuyang-liu16/VidCom2" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/VidCom2?style=social"></a>

<a href="https://arxiv.org/abs/2501.05179" target="_blank"><img src="https://img.shields.io/badge/arXiv-2501.05179-B31B1B?style=flat-square"></a> <u>Xuyang Liu</u>, Ziming Wang, Yuhang Han, Yingyao Wang, Jiale Yuan, Jun Song, Bo Zheng, Linfeng Zhang, Siteng Huang, Honggang Chen, &quot;**Global Compression Commander: Plug-and-Play Inference Acceleration for High-Resolution Large Vision-Language Models**&quot;. *arXiv preprint arXiv:2501.05179*. [[paper](https://arxiv.org/pdf/2501.05179)] [[code](https://github.com/xuyang-liu16/GlobalCom2)] <a href="https://github.com/xuyang-liu16/GlobalCom2" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16/GlobalCom2?style=social"></a>

<a href="https://arxiv.org/abs/2411.17686" target="_blank"><img src="https://img.shields.io/badge/arXiv-2411.17686-B31B1B?style=flat-square"></a> Yuhang Han<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Pengxiang Ding, Donglin Wang, Honggang Chen, Qingsen Yan, Siteng Huang &quot;**Filter, Correlate, Compress: Training-Free Token Reduction for MLLM Acceleration**&quot;. *arXiv preprint arXiv:2411.17686*. [[paper](https://arxiv.org/pdf/2411.17686)] [[page](https://ficoco-accelerate.github.io/)] [[code](https://github.com/kawhiiiileo/FiCoCo)] <a href="https://github.com/kawhiiiileo/FiCoCo" target="_blank"><img src="https://img.shields.io/github/stars/kawhiiiileo/FiCoCo?style=social"></a>

<a href="https://arxiv.org/abs/2405.14700" target="_blank"><img src="https://img.shields.io/badge/arXiv-2405.14700-B31B1B?style=flat-square"></a> Ting Liu<sup>\*</sup>, <u>Xuyang Liu</u><sup>\*</sup>, Siteng Huang, Liangtao Shi, Zunnan Xu , Yi Xin, Quanjun Yin &quot;**Sparse-Tuning: Adapting Vision Transformers with Efficient Fine-tuning and Inference**&quot;. *arXiv preprint arXiv:2405.14700*. [[paper](https://arxiv.org/pdf/2405.14700)] [[github](https://github.com/liuting20/Sparse-Tuning)] [[Chinese intro (Zhihu)](https://zhuanlan.zhihu.com/p/702216557)] <a href="https://github.com/liuting20/Sparse-Tuning" target="_blank"><img src="https://img.shields.io/github/stars/liuting20/Sparse-Tuning?style=social"></a>



## 🤗 Resources
Please find my full repositories on my [GitHub](https://github.com/xuyang-liu16) profile. <a href="https://github.com/xuyang-liu16" target="_blank"><img src="https://img.shields.io/github/stars/xuyang-liu16.svg?style=social" alt="GitHub"></a>

* [Awesome Generation Acceleration](https://github.com/xuyang-liu16/Awesome-Generation-Acceleration) [![GitHub](https://img.shields.io/github/stars/xuyang-liu16/Awesome-Generation-Acceleration.svg?style=social)](https://github.com/xuyang-liu16/Awesome-Generation-Acceleration.git)
  * Duty: Owner.
  * Description: An open-source repository that curates a collection of recent awesome papers on AIGC acceleration.
 
* [Awesome Token-level Model Compression](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression) [![GitHub](https://img.shields.io/github/stars/xuyang-liu16/Awesome-Token-level-Model-Compression.svg?style=social)](https://github.com/xuyang-liu16/Awesome-Token-level-Model-Compression.git)
  * Duty: Owner.
  * Description: An open-source repository that curates a collection of recent awesome papers on token-level model compression.
 
<!-- 
* [Awesome Parameter-Efficient Transfer Learning](https://github.com/synbol/Awesome-Parameter-Efficient-Transfer-Learning) [![GitHub](https://img.shields.io/github/stars/synbol/Awesome-Parameter-Efficient-Transfer-Learning.svg?style=social)](https://github.com/synbol/Awesome-Parameter-Efficient-Transfer-Learning.git)
  * Duty: Contributor.
  * Description: An open-source repository that curates a collection of recent awesome papers on parameter-efficient transfer learning. 
-->


## 💻 Experiences

### Internships

* Research Intern - **OPPO Research Institute, OPPO**, Shenzhen
  * Time: Jul 2025 - Present.
  * Thesis: *On-device Vision-language Models*.
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


## 🎖️ Honors

* 2025 **Master's First Prize Scholarship** in  Sichuan University
* 2025 Suzhou Industrial Park Scholarship, 2024 (**12 Students** in Sichuan University).


## 📠 Services

### Conference Reviewer
* Advances in Neural Information Processing Systems ([NeurIPS](https://neurips.cc/))
* AAAI Conference on Artificial Intelligence ([AAAI](https://aaai.org/conference/aaai/))
* ACM International Conference on Multimedia ([MM](https://2024.acmmm.org/))

