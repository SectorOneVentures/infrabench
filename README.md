# InfraBench — Cloud GPU VRAM Calculator & Web Scraping API Benchmarks

Live interactive suite: **[https://sectoroneventures.github.io/infrabench/](https://sectoroneventures.github.io/infrabench/)**

InfraBench is a real-time hardware sizing and cloud cost comparison suite for engineers provisioning GPU compute nodes or high-concurrency headless browser extraction pipelines.

---

## Features

1. **Exact GPU VRAM & KV-Cache Sizing Calculator**
   - Computes model weights memory, GQA/MHA KV-cache footprint (FP16 vs. FP8 KV compression), and CUDA activation buffers across `8B` to `671B` parameter architectures.
   - Determines minimum single-node or multi-GPU tensor-parallel (`TP=1, 2, 4, 8`) topologies across **H200 (141GB)**, **H100 NVL (94GB)**, **H100 SXM (80GB)**, **RTX PRO 6000 (96GB)**, **A100 (80GB)**, **L40S (48GB)**, **RTX 5090 (32GB)**, **RTX 4090 (24GB)**, and **RTX 3090 (24GB)**.
   - Pulls live verified on-demand $/hr telemetry from **[Vast.ai GPU Cloud](https://cloud.vast.ai/?ref_id=infrabench)** and compares hourly and monthly TCO against RunPod, Lambda, GCP, and AWS.

2. **Headless Browser & Anti-Bot Scraping API Benchmark Matrix**
   - Compares total monthly extraction cost, P50 latency, and anti-bot bypass success rates across **[Apify](https://apify.com/?fpr=infrabench)**, **[ScrapingBee](https://www.scrapingbee.com/?fpr=infrabench)**, Bright Data, and self-hosted Playwright container clusters.

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

* **[Browse Live Verified GPU Nodes on Vast.ai →](https://cloud.vast.ai/?ref_id=infrabench)**
* **[Launch Managed Headless Browser Actors on Apify →](https://apify.com/?fpr=infrabench)**
* **[Test Stealth Chrome Rendering API on ScrapingBee (1,000 Free Credits) →](https://www.scrapingbee.com/?fpr=infrabench)**

---

## License
MIT
