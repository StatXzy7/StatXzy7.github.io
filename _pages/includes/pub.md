<section class="home-section research-section" id="publications" aria-labelledby="research-title">
  <div class="section-heading">
    <div><p class="eyebrow">Selected work</p><h2 id="research-title">Research</h2></div>
    <a class="section-action" href="{{ site.author.googlescholar }}" target="_blank" rel="noopener noreferrer">All publications <span aria-hidden="true">↗</span></a>
  </div>
  <ul class="research-topics research-filters" aria-label="Filter publications by topic" hidden>
    <li><button type="button" data-research-filter="all" aria-pressed="true" aria-controls="research-paper-list">All <span class="filter-count" aria-hidden="true"></span></button></li>
    <li><button type="button" data-research-filter="medical-imaging" aria-pressed="false" aria-controls="research-paper-list">Medical imaging <span class="filter-count" aria-hidden="true"></span></button></li>
    <li><button type="button" data-research-filter="spatial-transcriptomics" aria-pressed="false" aria-controls="research-paper-list">Spatial transcriptomics <span class="filter-count" aria-hidden="true"></span></button></li>
    <li><button type="button" data-research-filter="knowledge-editing" aria-pressed="false" aria-controls="research-paper-list">Knowledge editing <span class="filter-count" aria-hidden="true"></span></button></li>
    <li><button type="button" data-research-filter="biological-sequences" aria-pressed="false" aria-controls="research-paper-list">Biological sequences <span class="filter-count" aria-hidden="true"></span></button></li>
  </ul>
  <p class="research-filter-status visually-hidden" role="status" aria-live="polite" aria-atomic="true"></p>

  <div id="research-paper-list">
  <article class="research-paper" data-paper-topics="medical-imaging">
    <a class="paper-visual" href="{{ '/images/sfibai-flowchart.png' | relative_url }}" target="_blank" rel="noopener noreferrer" aria-label="View the full SFibAI framework diagram"><img src="{{ '/images/sfibai-flowchart.png' | relative_url }}" alt="SFibAI ultrasound fibrosis grading and deployment framework" width="180" height="150" loading="lazy"></a>
    <div class="paper-content">
      <p class="paper-meta"><span class="paper-venue">Nature Communications · 2026</span><span class="paper-category">Medical imaging</span></p>
      <h3><a href="https://www.nature.com/articles/s41467-026-76287-9">Deep Learning for Precision Grading of Schistosoma Japonicum-induced Liver Fibrosis in Ultrasound Images</a></h3>
      <p class="paper-authors"><strong>Ziyang Xu</strong>, Jianfeng Zhang, Tingting Wu, Haiyong Hua, Kun Yang, <a href="https://www.math.cuhk.edu.hk/~zeng/">Tieyong Zeng</a></p>
      <p class="paper-description">SFibAI grades liver fibrosis from ultrasound, trained on 167,702 images across 36 stages. The framework includes a Windows/Android SDK.</p>
      <div class="paper-links"><a href="https://www.nature.com/articles/s41467-026-76287-9">Paper <span aria-hidden="true">↗</span></a><a href="https://github.com/StatXzy7/SFibAI">Code <span aria-hidden="true">↗</span></a></div>
      <details class="paper-details" data-abstract-source="https://www.nature.com/articles/s41467-026-76287-9?error=cookies_not_supported"><summary>Abstract</summary>
        <p class="paper-abstract">Liver fibrosis caused by schistosomiasis is a major health problem in endemic regions. Ultrasonography is widely used for screening, but grading remains subjective and dependent on specialist expertise. Here we show that a deep learning system can provide automated, fine-grained assessment of liver fibrosis caused by Schistosoma japonicum. We developed and evaluated the system using a multicentre dataset of 167,702 ultrasound images labelled on a 36-level scale from 0.0 to 3.5, designed to capture gradual disease progression and map onto four clinical grades. Of these images, 16,811 were reserved for the independent test set. In this test set, 93.9% of predictions were within 0.5 grades of expert labels, with a mean absolute error of 0.116. We further developed a deployable version that ran on Windows and Android devices, processing each image in less than 400 milliseconds. These results support scalable and more consistent ultrasound screening and follow-up in endemic regions.</p>
      </details>
    </div>
  </article>

  <article class="research-paper" data-paper-topics="medical-imaging spatial-transcriptomics">
    <a class="paper-visual" href="{{ '/images/focst.png' | relative_url }}" target="_blank" rel="noopener noreferrer" aria-label="View the full FOCST histology-to-transcriptomics framework"><img src="{{ '/images/focst.png' | relative_url }}" alt="FOCST histology-to-transcriptomics framework" width="180" height="150" loading="lazy"></a>
    <div class="paper-content">
      <p class="paper-meta"><span class="paper-venue">PLOS Computational Biology · 2026</span><span class="paper-category">Medical imaging · Spatial transcriptomics</span></p>
      <h3><a href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1014762">Spatially Guided Translation from Histology Images to Transcriptomic Profiles Using Foundation Model-Driven Contrastive Learning</a></h3>
      <p class="paper-authors">Zi Huai Huang, <strong>Ziyang Xu</strong>, <a href="https://phulab.org/">Pingzhao Hu</a></p>
      <p class="paper-description">Foundation-model features and spatially guided contrastive learning predict spatial transcriptomic profiles from histology images.</p>
      <div class="paper-links"><a href="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1014762">Paper <span aria-hidden="true">↗</span></a><a href="https://github.com/mattthuang/FOCST">Code <span aria-hidden="true">↗</span></a></div>
      <details class="paper-details" data-abstract-source="https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1014762"><summary>Abstract</summary>
        <p class="paper-abstract">Spatial transcriptomics (ST) enhances single-cell RNA sequencing by revealing transcript distribution, offering critical insights into heterogeneous diseases such as breast cancer. However, the high cost and lengthy processes of generating high-quality ST data limit clinical application. Recent deep learning methods predict ST from histology images, but often fail to capture both morphological features and spatial context. We introduce FOCST, a foundation model-driven framework for ST imputation that leverages spatial guided contrastive learning. FOCST begins with UNI, a large histopathology foundation model, to extract visual features from tissue images. These are integrated with expression data in a unified embedding space via contrastive learning, enabling cross-modal prediction and imputation. To further enhance spatial awareness, a graph neural network incorporates positional information, improving regional detection and interpretability.Benchmarking demonstrates FOCST’s superior performance over state-of-the-art methods and alternative vision encoders (paired Wilcoxon signed-rank tests, FDR-adjusted p &lt; 0.05, N = 6 images). Predicted profiles enable clinically relevant downstream analyses, including patient stratification by treatment response (ROC AUC (Receiver Operating Characteristic – Area Under the Curve) = 0.79). Our results highlight the promise of combining foundation models and spatially guided learning to efficiently generate ST insights, advancing cancer research and precision medicine.</p>
      </details>
    </div>
  </article>

  <article class="research-paper" data-paper-topics="knowledge-editing">
    <a class="paper-visual" href="{{ '/images/react.png' | relative_url }}" target="_blank" rel="noopener noreferrer" aria-label="View the full REACT framework diagram"><img src="{{ '/images/react.png' | relative_url }}" alt="REACT framework for controllable language model knowledge editing" width="180" height="150" loading="lazy"></a>
    <div class="paper-content">
      <p class="paper-meta"><span class="paper-venue">EMNLP Main · 2025</span><span class="paper-category">Knowledge editing</span></p>
      <h3><a href="https://aclanthology.org/2025.emnlp-main.860/">REACT: Representation Extraction And Controllable Tuning to Overcome Overfitting in LLM Knowledge Editing</a></h3>
      <p class="paper-authors"><a href="https://jzsawyer.github.io/">Haitian Zhong</a>, Yuhuan Liu, <strong>Ziyang Xu</strong>, Guofan Liu, Qiang Liu, Shu Wu, Zhe Zhao, Liang Wang, Tieniu Tan</p>
      <p class="paper-description">A two-stage framework for controllable LLM knowledge editing that reduces overfitting while preserving reliability, locality, and generality.</p>
      <div class="paper-links"><a href="https://aclanthology.org/2025.emnlp-main.860/">Paper <span aria-hidden="true">↗</span></a><a href="https://arxiv.org/abs/2505.18933">arXiv <span aria-hidden="true">↗</span></a></div>
      <details class="paper-details" data-abstract-source="https://aclanthology.org/2025.emnlp-main.860/"><summary>Abstract</summary>
        <p class="paper-abstract">Large language model editing methods frequently suffer from overfitting, wherein factual updates can propagate beyond their intended scope, overemphasizing the edited target even when it’s contextually inappropriate. To address this challenge, we introduce REACT (Representation Extraction And Controllable Tuning), a unified two-phase framework designed for precise and controllable knowledge editing. In the initial phase, we utilize tailored stimuli to extract latent factual representations and apply Principal Component Analysis with a simple learnbale linear transformation to compute a directional “belief shift” vector for each instance. In the second phase, we apply controllable perturbations to hidden states using the obtained vector with a magnitude scalar, gated by a pre-trained classifier that permits edits only when contextually necessary. Relevant experiments on EVOKE benchmarks demonstrate that REACT significantly reduces overfitting across nearly all evaluation metrics, and experiments on COUNTERFACT and MQuAKE shows that our method preserves balanced basic editing performance (reliability, locality, and generality) under diverse editing scenarios.</p>
      </details>
    </div>
  </article>

  <article class="research-paper" data-paper-topics="biological-sequences">
    <a class="paper-visual" href="{{ '/images/biologyinstructions.png' | relative_url }}" target="_blank" rel="noopener noreferrer" aria-label="View the full Biology-Instructions diagram"><img src="{{ '/images/biologyinstructions.png' | relative_url }}" alt="Biology-Instructions dataset and multi-omics language model benchmark" width="180" height="150" loading="lazy"></a>
    <div class="paper-content">
      <p class="paper-meta"><span class="paper-venue">EMNLP Findings · 2025</span><span class="paper-category">Biological sequences</span></p>
      <h3><a href="https://aclanthology.org/2025.findings-emnlp.978/">Biology-Instructions: A Dataset and Benchmark for Multi-Omics Sequence Understanding Capability of Large Language Models</a></h3>
      <p class="paper-authors"><a href="https://scholar.google.com/citations?user=6YRQTlQAAAAJ&amp;hl=zh-CN">Haonan He</a><sup>†</sup>, Yuchen Ren<sup>†</sup>, Yining Tang<sup>†</sup>, <strong>Ziyang Xu</strong><sup>†</sup>, Junxian Li, Minghao Yang, Di Zhang, Dong Yuan, Tao Chen, Shufei Zhang, Yuqiang Li, Nanqing Dong, Wanli Ouyang, Dongzhan Zhou, Peng Ye</p>
      <p class="paper-description">An instruction-tuning dataset and benchmark for DNA, RNA, proteins, and multi-molecule sequences, with ChatMultiOmics as a three-stage training baseline.</p>
      <div class="paper-links"><a href="https://aclanthology.org/2025.findings-emnlp.978/">Paper <span aria-hidden="true">↗</span></a><a href="https://github.com/hhnqqq/Biology-Instructions">Code <span aria-hidden="true">↗</span></a></div>
      <details class="paper-details" data-abstract-source="https://aclanthology.org/2025.findings-emnlp.978/"><summary>Abstract</summary>
        <p class="paper-abstract">Large language models (LLMs) have shown remarkable capabilities in general domains, but their application to multi-omics biology remains underexplored. To address this gap, we introduce Biology-Instructions, the first large-scale instruction-tuning dataset for multi-omics biological sequences, including DNA, RNA, proteins, and multi-molecules. This dataset bridges LLMs and complex biological sequence-related tasks, enhancing their versatility and reasoning while maintaining conversational fluency. We also highlight significant limitations of current state-of-the-art LLMs on multi-omics tasks without specialized training. To overcome this, we propose ChatMultiOmics, a strong baseline with a novel three-stage training pipeline, demonstrating superior biological understanding through Biology-Instructions. Both resources are publicly available, paving the way for better integration of LLMs in multi-omics analysis. The Biology-Instructions is publicly available at: https://github.com/hhnqqq/Biology-Instructions.</p>
      </details>
    </div>
  </article>

  <article class="research-paper" data-paper-topics="biological-sequences">
    <a class="paper-visual" href="{{ '/images/ptransips.png' | relative_url }}" target="_blank" rel="noopener noreferrer" aria-label="View the full PTransIPs framework diagram"><img src="{{ '/images/ptransips.png' | relative_url }}" alt="PTransIPs protein language model and transformer architecture" width="180" height="150" loading="lazy"></a>
    <div class="paper-content">
      <p class="paper-meta"><span class="paper-venue">IEEE J-BHI · 2024</span><span class="paper-category">Biological sequences</span></p>
      <h3><a href="https://ieeexplore.ieee.org/abstract/document/10472595/">PTransIPs: Identification of phosphorylation sites enhanced by protein PLM embeddings</a></h3>
      <p class="paper-authors"><strong>Ziyang Xu</strong><sup>†</sup>, <a href="https://jzsawyer.github.io/">Haitian Zhong</a><sup>†</sup>, Bingrui He, Xueying Wang, <a href="https://www.researchgate.net/profile/Tianchi-Lu-3">Tianchi Lu</a></p>
      <p class="paper-description">Protein language model embeddings and a transformer for phosphorylation-site prediction, with transductive information maximization for peptide bioactivity tasks.</p>
      <div class="paper-links"><a href="https://ieeexplore.ieee.org/abstract/document/10472595/">Paper <span aria-hidden="true">↗</span></a><a href="https://github.com/StatXzy7/PTransIPs">Code <span aria-hidden="true">↗</span></a></div>
      <details class="paper-details" data-abstract-source="https://arxiv.org/abs/2308.05115"><summary>Abstract</summary>
        <p class="paper-abstract">Phosphorylation is pivotal in numerous fundamental cellular processes and plays a significant role in the onset and progression of various diseases. The accurate identification of these phosphorylation sites is crucial for unraveling the molecular mechanisms within cells and during viral infections, potentially leading to the discovery of novel therapeutic targets. In this study, we develop PTransIPs, a new deep learning framework for the identification of phosphorylation sites. Independent testing results demonstrate that PTransIPs outperforms existing state-of-the-art (SOTA) methods, achieving AUCs of 0.9232 and 0.9660 for the identification of phosphorylated S/T and Y sites, respectively. PTransIPs contributes from three aspects. 1) PTransIPs is the first to apply protein pre-trained language model (PLM) embeddings to this task. It utilizes ProtTrans and EMBER2 to extract sequence and structure embeddings, respectively, as additional inputs into the model, effectively addressing issues of dataset size and overfitting, thus enhancing model performance; 2) PTransIPs is based on Transformer architecture, optimized through the integration of convolutional neural networks and TIM loss function, providing practical insights for model design and training; 3) The encoding of amino acids in PTransIPs enables it to serve as a universal framework for other peptide bioactivity tasks, with its excellent performance shown in extended experiments of this paper. Our code, data and models are publicly available at https://github.com/StatXzy7/PTransIPs.</p>
      </details>
    </div>
  </article>
  </div>
  <p class="research-tools"><span>Tools &amp; practice</span> Agent evaluation · Tool use · PyTorch · Transformers · Multimodal learning</p>
</section>
