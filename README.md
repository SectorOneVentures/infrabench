# InfraBench — Cloud GPU VRAM Calculator & Web Scraping API Benchmarks

Live interactive suite: **[https://sectoroneventures.github.io/infrabench/](https://sectoroneventures.github.io/infrabench/)**

InfraBench is a real-time hardware sizing and cloud cost comparison suite for engineers provisioning GPU compute nodes or high-concurrency headless browser extraction pipelines.

---

## Features

1. **Exact GPU VRAM & KV-Cache Sizing Calculator**
   - Computes model weights memory, GQA/MHA KV-cache footprint (FP16 vs. FP8 KV compression), and CUDA activation buffers across `8B` to `671B` parameter architectures.
   - Determines minimum single-node or multi-GPU tensor-parallel (`TP=1, 2, 4, 8`) topologies across **H200 (141GB)**, **H100 NVL (94GB)**, **H100 SXM (80GB)**, **RTX PRO 6000 (96GB)**, **A100 (80GB)**, **L40S (48GB)**, **RTX 5090 (32GB)**, **RTX 4090 (24GB)**, and **RTX 3090 (24GB)**.
   - Pulls live verified on-demand $/hr telemetry from **[Vast.ai GPU Cloud](https://cloud.vast.ai/?ref_id=749467)** and compares hourly and monthly TCO against RunPod, Lambda, GCP, and AWS.

2. **1-Click Verified GPU Container Templates (Vast.ai Public Library)**
   - **[vLLM OpenAI API Server (FP8 KV-Cache + AWQ Ready)](https://cloud.vast.ai/?ref_id=749467&template_id=f702973989cc33171c27cf3db6d5a545)**
   - **[DeepSeek-R1 & Qwen2.5-72B SGLang High-Throughput Server](https://cloud.vast.ai/?ref_id=749467&template_id=5bdd3dd59970ee8c778a596bad88b6ee)**
   - **[Ollama + Open WebUI Private Model Server (1-Click)](https://cloud.vast.ai/?ref_id=749467&template_id=a157e8865a334938872f9e1bbcc1573a)**
   - **[Unsloth Fast Fine-Tuning & QLoRA Training Studio (CUDA 12.8)](https://cloud.vast.ai/?ref_id=749467&template_id=2c8267748fc42b4cf6c75fe4200afb47)**
   - **[ComfyUI Flux.1 Dev + Wan2.1 Video Generation Studio](https://cloud.vast.ai/?ref_id=749467&template_id=a703d9051cbf75e7464128527f7bfe6d)**

3. **Zero-Dependency CLI Calculator (`cli.py`)**
   ```bash
   python3 cli.py --params 70 --quant 4.5 --ctx 32768 --batch 4
   ```

---

## Quick Comparison Snapshot (Live Verified Market Floor)

| GPU Model | VRAM | Vast.ai Verified $/hr | RunPod $/hr | AWS On-Demand Eq. | Savings vs AWS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RTX 3090** | 24 GB | **$0.19/hr** | $0.34/hr | $1.45/hr | **86.9%** |
| **RTX 4090** | 24 GB | **$0.36/hr** | $0.59/hr | $1.95/hr | **81.5%** |
| **RTX 5090** | 32 GB | **$0.67/hr** | $0.89/hr | $2.40/hr | **72.1%** |
| **L40S** | 48 GB | **$0.68/hr** | $0.86/hr | $2.85/hr | **76.1%** |
| **A100 PCIE** | 80 GB | **$0.89/hr** | $1.19/hr | $3.80/hr | **76.6%** |
| **RTX PRO 6000** | 96 GB | **$1.23/hr** | $1.89/hr | $4.50/hr | **72.7%** |
| **H100 SXM** | 80 GB | **$2.30/hr** | $2.69/hr | $6.88/hr | **66.5%** |

* **[Browse Live Verified GPU Nodes on Vast.ai →](https://cloud.vast.ai/?ref_id=749467)**
* **[FastSEOHub Automated SERP & Indexing Pipeline →](https://www.digistore24.com/redir/676823/infrabench7552/)**
* **[n8n Self-Hosted Workflow & Webhook Extraction Blueprint →](https://www.checkout-ds24.com/redir/667670/infrabench7552/)**
* **[Tube Magic Automated Video Pipeline SaaS →](https://www.digistore24.com/redir/540531/infrabench7552/)**

---

## License
MIT
