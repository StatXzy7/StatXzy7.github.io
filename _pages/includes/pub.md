<section class="home-section research-section" id="publications" aria-labelledby="research-title">
  <div class="section-heading">
    <div><p class="eyebrow">Selected work</p><h2 id="research-title">Research</h2></div>
    <a class="section-action" href="{{ site.author.googlescholar }}" target="_blank" rel="noopener noreferrer">All publications <span aria-hidden="true">↗</span></a>
  </div>
  <p class="section-intro">From language models to scientific and medical imaging.</p>
  <ul class="research-topics" aria-label="Research interests"><li>Reinforcement learning</li><li>On-policy distillation</li><li>Image processing</li></ul>

  <article class="research-paper">
    <a class="paper-visual" href="{{ '/images/sfibai-flowchart.png' | relative_url }}" target="_blank" rel="noopener noreferrer" aria-label="View the full SFibAI framework diagram"><img src="{{ '/images/sfibai-flowchart.png' | relative_url }}" alt="SFibAI ultrasound fibrosis grading and deployment framework" width="180" height="150" loading="lazy"></a>
    <div class="paper-content">
      <p class="paper-meta"><span class="paper-venue">Nature Communications · 2026</span><span class="paper-category">AI for Science</span></p>
      <h3><a href="https://www.nature.com/articles/s41467-026-76287-9">Deep Learning for Precision Grading of Schistosoma Japonicum-induced Liver Fibrosis in Ultrasound Images</a></h3>
      <p class="paper-authors"><strong>Ziyang Xu</strong>, Jianfeng Zhang, Tingting Wu, Haiyong Hua, Kun Yang, <a href="https://www.math.cuhk.edu.hk/~zeng/">Tieyong Zeng</a></p>
      <p class="paper-description">SFibAI grades liver fibrosis from ultrasound, trained on 167,702 images across 36 stages. The framework includes a Windows/Android SDK.</p>
      <div class="paper-links"><a href="https://www.nature.com/articles/s41467-026-76287-9">Paper <span aria-hidden="true">↗</span></a><a href="https://github.com/StatXzy7/SFibAI">Code <span aria-hidden="true">↗</span></a></div>
      <details class="paper-details"><summary>Abstract &amp; details</summary>
        <ul>
          <li><strong>Status:</strong> Published online in Nature Communications, August 2026.</li>
          <li><strong>Work:</strong> We developed SFibAI, an end-to-end deep learning framework for fine-grained fibrosis grading from B-mode ultrasound, trained on a large-scale multi-center dataset of 167,702 images with 36 discrete fibrosis stages.</li>
          <li><strong>Performance:</strong> Designed a hybrid KL/MSE/boundary-sensitive loss, achieving 93.9% accuracy within ±0.5 stages and MAE 0.116 on 16,811 independent test images.</li>
          <li><strong>Deployment:</strong> Built a Windows/Android SDK with average per-image latency below 400 ms.</li>
        </ul>
      </details>
    </div>
  </article>

  <article class="research-paper">
    <a class="paper-visual" href="{{ '/images/react.png' | relative_url }}" target="_blank" rel="noopener noreferrer" aria-label="View the full REACT framework diagram"><img src="{{ '/images/react.png' | relative_url }}" alt="REACT framework for controllable language model knowledge editing" width="180" height="150" loading="lazy"></a>
    <div class="paper-content">
      <p class="paper-meta"><span class="paper-venue">EMNLP Main · 2025</span><span class="paper-category">Language Models</span></p>
      <h3><a href="https://aclanthology.org/2025.emnlp-main.860/">REACT: Representation Extraction And Controllable Tuning to Overcome Overfitting in LLM Knowledge Editing</a></h3>
      <p class="paper-authors"><a href="https://jzsawyer.github.io/">Haitian Zhong</a>, Yuhuan Liu, <strong>Ziyang Xu</strong>, Guofan Liu, Qiang Liu, Shu Wu, Zhe Zhao, Liang Wang, Tieniu Tan</p>
      <p class="paper-description">A two-stage framework for controllable LLM knowledge editing that reduces overfitting while preserving reliability, locality, and generality.</p>
      <div class="paper-links"><a href="https://aclanthology.org/2025.emnlp-main.860/">Paper <span aria-hidden="true">↗</span></a><a href="https://arxiv.org/abs/2505.18933">arXiv <span aria-hidden="true">↗</span></a></div>
      <details class="paper-details"><summary>Abstract &amp; details</summary>
        <p>Large language model editing methods frequently suffer from overfitting, wherein factual updates can propagate beyond their intended scope, overemphasizing the edited target even when it's contextually inappropriate. To address this challenge, we introduce REACT (Representation Extraction And Controllable Tuning), a unified two-phase framework designed for precise and controllable knowledge editing. In the initial phase, we utilize tailored stimuli to extract latent factual representations and apply Principal Component Analysis with a simple learnable linear transformation to compute a directional "belief shift" vector for each instance. In the second phase, we apply controllable perturbations to hidden states using the obtained vector with a magnitude scalar, gated by a pre-trained classifier that permits edits only when contextually necessary. Relevant experiments on EVOKE benchmarks demonstrate that REACT significantly reduces overfitting across nearly all evaluation metrics, and experiments on COUNTERFACT and MQuAKE show that our method preserves balanced basic editing performance (reliability, locality, and generality) under diverse editing scenarios.</p>
      </details>
    </div>
  </article>

  <article class="research-paper">
    <a class="paper-visual" href="{{ '/images/biologyinstructions.png' | relative_url }}" target="_blank" rel="noopener noreferrer" aria-label="View the full Biology-Instructions diagram"><img src="{{ '/images/biologyinstructions.png' | relative_url }}" alt="Biology-Instructions dataset and multi-omics language model benchmark" width="180" height="150" loading="lazy"></a>
    <div class="paper-content">
      <p class="paper-meta"><span class="paper-venue">EMNLP Findings · 2025</span><span class="paper-category">Language Models</span></p>
      <h3><a href="https://aclanthology.org/2025.findings-emnlp.978/">Biology-Instructions: A Dataset and Benchmark for Multi-Omics Sequence Understanding Capability of Large Language Models</a></h3>
      <p class="paper-authors"><a href="https://scholar.google.com/citations?user=6YRQTlQAAAAJ&amp;hl=zh-CN">Haonan He</a><sup>†</sup>, Yuchen Ren<sup>†</sup>, Yining Tang<sup>†</sup>, <strong>Ziyang Xu</strong><sup>†</sup>, Junxian Li, Minghao Yang, Di Zhang, Dong Yuan, Tao Chen, Shufei Zhang, Yuqiang Li, Nanqing Dong, Wanli Ouyang, Dongzhan Zhou, Peng Ye</p>
      <p class="paper-description">An instruction-tuning dataset and benchmark for DNA, RNA, proteins, and multi-molecule sequences, with ChatMultiOmics as a three-stage training baseline.</p>
      <div class="paper-links"><a href="https://aclanthology.org/2025.findings-emnlp.978/">Paper <span aria-hidden="true">↗</span></a><a href="https://github.com/hhnqqq/Biology-Instructions">Code <span aria-hidden="true">↗</span></a></div>
      <details class="paper-details"><summary>Abstract &amp; details</summary>
        <p>Large language models (LLMs) have shown remarkable capabilities in general domains, but their application to multi-omics biology remains underexplored. To address this gap, we introduce Biology-Instructions, the first large-scale instruction-tuning dataset for multi-omics biological sequences, including DNA, RNA, proteins, and multi-molecules. This dataset bridges LLMs and complex biological sequence-related tasks, enhancing their versatility and reasoning while maintaining conversational fluency. We also highlight significant limitations of current state-of-the-art LLMs on multi-omics tasks without specialized training. To overcome this, we propose ChatMultiOmics, a strong baseline with a novel three-stage training pipeline, demonstrating superior biological understanding through Biology-Instructions. Both resources are publicly available, paving the way for better integration of LLMs in multi-omics analysis.</p>
      </details>
    </div>
  </article>

  <article class="research-paper">
    <a class="paper-visual" href="{{ '/images/ptransips.png' | relative_url }}" target="_blank" rel="noopener noreferrer" aria-label="View the full PTransIPs framework diagram"><img src="{{ '/images/ptransips.png' | relative_url }}" alt="PTransIPs protein language model and transformer architecture" width="180" height="150" loading="lazy"></a>
    <div class="paper-content">
      <p class="paper-meta"><span class="paper-venue">IEEE J-BHI · 2024</span><span class="paper-category">AI for Science</span></p>
      <h3><a href="https://ieeexplore.ieee.org/abstract/document/10472595/">PTransIPs: Identification of phosphorylation sites enhanced by protein PLM embeddings</a></h3>
      <p class="paper-authors"><strong>Ziyang Xu</strong><sup>†</sup>, <a href="https://jzsawyer.github.io/">Haitian Zhong</a><sup>†</sup>, Bingrui He, Xueying Wang, <a href="https://www.researchgate.net/profile/Tianchi-Lu-3">Tianchi Lu</a></p>
      <p class="paper-description">Protein language model embeddings and a transformer for phosphorylation-site prediction, with transductive information maximization for peptide bioactivity tasks.</p>
      <div class="paper-links"><a href="https://ieeexplore.ieee.org/abstract/document/10472595/">Paper <span aria-hidden="true">↗</span></a><a href="https://github.com/StatXzy7/PTransIPs">Code <span aria-hidden="true">↗</span></a></div>
      <details class="paper-details"><summary>Abstract &amp; details</summary>
        <ul>
          <li><strong>Work:</strong> We present PTransIPs, a new deep learning framework for the identification of phosphorylation sites in host cells infected with SARS-CoV-2. It utilizes protein pre-trained language model (PLM) embeddings and transformer structure to make the final prediction, with transductive information maximization (TIM) loss to better evaluate the error. PTransIPs is also a universal framework for all peptide bioactivity tasks.</li>
          <li><strong>Performance:</strong> After comparing PTransIPs with five existing phosphorylation site prediction tools, we notice it achieves the best performance in all five model evaluation metrics (ACC, SEN, SPEC, MCC, AUC) for both S/T and Y sites.</li>
          <li><strong>Impact:</strong> We hope that PTransIPs will aid in deepening the understanding of SARS-CoV-2 phosphorylation sites and look forward to enhancing PTransIPs in the future to become a more powerful tool for the scientific community.</li>
        </ul>
      </details>
    </div>
  </article>
  <p class="research-tools"><span>Tools &amp; practice</span> PyTorch · Transformers · LoRA/SFT · Distributed training · On-device AI deployment</p>
</section>
