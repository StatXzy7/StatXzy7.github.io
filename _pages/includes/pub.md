# 📝 Publications

## 💻 Large Language Models

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">``EMNLP 2025``</div><img src='images/react.png' alt="sy   m" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

 [**REACT**: **R**epresentation **E**xtraction **A**nd **C**ontrollable **T**uning to Overcome Overfitting in LLM Knowledge Editing](https://aclanthology.org/2025.emnlp-main.860/) \\
[Haitian Zhong](https://jzsawyer.github.io/), Yuhuan Liu, **Ziyang Xu**, Guofan Liu, Qiang Liu, Shu Wu, Zhe Zhao, Liang Wang, Tieniu Tan

- **Abstract**: Large language model editing methods frequently suffer from overfitting, wherein factual updates can propagate beyond their intended scope, overemphasizing the edited target even when it's contextually inappropriate. To address this challenge, we introduce **REACT** (**R**epresentation **E**xtraction **A**nd **C**ontrollable **T**uning), a unified two-phase framework designed for precise and controllable knowledge editing. In the initial phase, we utilize tailored stimuli to extract latent factual representations and apply Principal Component Analysis with a simple learnbale linear transformation to compute a directional "belief shift" vector for each instance. In the second phase, we apply controllable perturbations to hidden states using the obtained vector with a magnitude scalar, gated by a pre-trained classifier that permits edits only when contextually necessary. Relevant experiments on EVOKE benchmarks demonstrate that **REACT** significantly reduces overfitting across nearly all evaluation metrics, and experiments on COUNTERFACT and MQuAKE shows that our method preserves balanced basic editing performance (reliability, locality, and generality) under diverse editing scenarios.

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">``EMNLP 2025``</div><img src='images/biologyinstructions.png' alt="sy   m" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

 [Biology-Instructions: A Dataset and Benchmark for Multi-Omics Sequence Understanding Capability of Large Language Models](https://aclanthology.org/2025.findings-emnlp.978/) \\
[Haonan He]{https://scholar.google.com/citations?user=6YRQTlQAAAAJ&hl=zh-CN}`<sup>`&dagger;`</sup>`, Yuchen Ren`<sup>`&dagger;`</sup>`, Yining Tang`<sup>`&dagger;`</sup>`, **Ziyang Xu**`<sup>`&dagger;`</sup>`, Junxian Li, Minghao Yang, Di Zhang, Yuan Dong, Tao Chen, Shufei Zhang, Yuqiang Li, Nanqing Dong, Wanli Ouyang, Dongzhan Zhou, Peng Ye

- **Abstract**: Large language models (LLMs) have shown remarkable capabilities in general domains, but their application to multi-omics biology remains underexplored. To address this gap, we introduce Biology-Instructions, the first large-scale instruction-tuning dataset for multi-omics biological sequences, including DNA, RNA, proteins, and multi-molecules. This dataset bridges LLMs and complex biological sequence-related tasks, enhancing their versatility and reasoning while maintaining conversational fluency. We also highlight significant limitations of current state-of-the-art LLMs on multi-omics tasks without specialized training. To overcome this, we propose ChatMultiOmics, a strong baseline with a novel three-stage training pipeline, demonstrating superior biological understanding through Biology-Instructions. Both resources are publicly available, paving the way for better integration of LLMs in multi-omics analysis. The Biology-Instructions is publicly available at: https://github.com/hhnqqq/Biology-Instructions.
- **Codes**: [![](https://img.shields.io/github/stars/hhnqqq/Biology-Instructions?style=social&label=Biology-Instructions)](https://github.com/hhnqqq/Biology-Instructions)

</div>
</div>



## 🧬 AI for Science

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE J-BHI</div><img src='images/ptransips.png' alt="sy   m" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PTransIPs: Identification of phosphorylation sites enhanced by protein PLM embeddings](https://ieeexplore.ieee.org/abstract/document/10472595/) \\
**Ziyang Xu** `<sup>`&dagger;`</sup>`, [Haitian Zhong](https://jzsawyer.github.io/) `<sup>`&dagger;`</sup>`, Bingrui He, Xueying Wang, [Tianchi Lu](https://www.researchgate.net/profile/Tianchi-Lu-3)

- **Work**: We present PTransIPs, **a new deep learning framework for the identification of phosphorylation sites** in host cells infected with SARS-CoV-2. It utilizes protein pre-trained language model (PLM) embeddings and transformer structure to make the final prediction, with transductive information maximization (TIM) loss to better evaluate the error. PTransIPs is also a universal framework for all peptide bioactivity tasks.
- **Performance**: After comparing PTransIPs with five existing phosphorylation site prediction tools, we notice it achieves **the best performance in all five model evaluation metrics (ACC, SEN, SPEC, MCC, AUC) for both S/T and Y sites**.
- **Impact**: We hope that PTransIPs will aid in deepening the understanding of SARS-CoV-2 phosphorylation sites and look forward to enhancing PTransIPs in the future to become a more powerful tool for the scientific community.
- **Codes**: [![](https://img.shields.io/github/stars/StatXzy7/PTransIPs?style=social&label=PTransIPs)](https://github.com/StatXzy7/PTransIPs)

</div>
</div>



<!-- ## 📄 Manuscripts -->
