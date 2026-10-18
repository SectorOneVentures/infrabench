# InfraBench — Simple GPU Memory Calculator, Web Scraping API Benchmarks & Cloud Cost Tools

Live calculators:
* **GPU Memory & Hourly Price Calculator:** **[https://sectoroneventures.github.io/infrabench/](https://sectoroneventures.github.io/infrabench/)**
* **Headless Browser & Scraping API Cost Calculator:** **[https://sectoroneventures.github.io/infrabench/headless-scraper-benchmark.html](https://sectoroneventures.github.io/infrabench/headless-scraper-benchmark.html)**
* **Self-Hosted Docker vs. Cloud Scraper TCO Estimator:** **[https://sectoroneventures.github.io/infrabench/docker-vps-tco-estimator.html](https://sectoroneventures.github.io/infrabench/docker-vps-tco-estimator.html)**

I got tired of guessing how much GPU memory I needed before renting a cloud box (or getting hit with unexpected proxy bills when running headless Chrome scrapers), so I put together these quick calculators and daily price sheets.

---

## What It Does

1. **Checks How Much GPU Memory You Actually Need**
   - Shows the memory needed for the model weights, the context window (KV cache), and a small safety buffer so your container doesn't crash.
   - Tells you right away if a model fits on a single card (like an **RTX 3090 24GB**, **RTX 4090 24GB**, **RTX 5090 32GB**, or **L40S 48GB**) or if you need multiple GPUs (**A100 80GB**, **H100**, **H200**).
   - Pulls live hourly rental prices from **[Vast.ai](https://cloud.vast.ai/?ref_id=749467)** so you can see how much cheaper it is compared to RunPod or AWS.

2. **Compares Headless Browser & Anti-Bot Scraping APIs**
   - Interactive monthly price and anti-bot bypass calculator comparing **[Apify](https://apify.com?fpr=infrabench7552)** ($5/mo free credit + 2,000+ ready-made actors), **[ScrapingBee](https://www.scrapingbee.com?fpr=infrabench7552)** (1,000 free API calls with stealth Chrome proxies), and self-hosted Playwright containers on **[Vast.ai](https://cloud.vast.ai/?ref_id=749467)**.

3. **1-Click Ready-to-Run GPU Templates (on Vast.ai)**
   If you don't want to mess around with Docker flags and CUDA versions, you can launch these directly:
   - **[vLLM Server (FP8 Cache + AWQ Ready)](https://cloud.vast.ai/?ref_id=749467&template_id=f702973989cc33171c27cf3db6d5a545)**
   - **[DeepSeek-R1 & Qwen2.5-72B Fast SGLang Server](https://cloud.vast.ai/?ref_id=749467&template_id=5bdd3dd59970ee8c778a596bad88b6ee)**
   - **[Ollama + Open WebUI Private Server (1-Click)](https://cloud.vast.ai/?ref_id=749467&template_id=a157e8865a334938872f9e1bbcc1573a)**
   - **[Unsloth Fine-Tuning & QLoRA Notebook (CUDA 12.8)](https://cloud.vast.ai/?ref_id=749467&template_id=2c8267748fc42b4cf6c75fe4200afb47)**
   - **[ComfyUI Flux.1 Dev + Wan2.1 Video Studio](https://cloud.vast.ai/?ref_id=749467&template_id=a703d9051cbf75e7464128527f7bfe6d)**

4. **Simple Command-Line Script (`cli.py`)**
   No extra packages needed — just run it with Python:
   ```bash
   python3 cli.py --params 70 --quant 4.5 --ctx 32768 --batch 4
   ```

---

## Current Cheapest Hourly GPU Prices

| GPU Card | Memory | Vast.ai Price | RunPod Price | AWS Price | What You Save |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RTX 3090** | 24 GB | **$0.19/hr** | $0.34/hr | $1.45/hr | **86.9%** |
| **RTX 4090** | 24 GB | **$0.35/hr** | $0.59/hr | $1.95/hr | **82.0%** |
| **RTX 5090** | 32 GB | **$0.67/hr** | $0.89/hr | $2.40/hr | **72.1%** |
| **L40S** | 48 GB | **$0.46/hr** | $0.86/hr | $2.85/hr | **83.9%** |
| **A100 PCIE** | 80 GB | **$0.79/hr** | $1.19/hr | $3.80/hr | **79.2%** |
| **RTX PRO 6000** | 96 GB | **$1.11/hr** | $1.89/hr | $4.50/hr | **75.3%** |
| **H100 SXM** | 80 GB | **$1.93/hr** | $2.69/hr | $6.88/hr | **71.9%** |

### Quick Links & Tools
* **[Headless Browser & Scraping API Benchmark →](https://sectoroneventures.github.io/infrabench/headless-scraper-benchmark.html)**
* **[Docker vs. Cloud Scraper TCO Estimator →](https://sectoroneventures.github.io/infrabench/docker-vps-tco-estimator.html)**
* **[DeepSeek-R1 & Qwen 72B Memory & GPU Price Guide →](https://sectoroneventures.github.io/infrabench/deepseek-r1-vram-pricing-guide.html)**
* **[Apify Cloud Scrapers ($5/mo Free Credit) →](https://apify.com?fpr=infrabench7552)**
* **[ScrapingBee Stealth Proxy API (1,000 Free Calls) →](https://www.scrapingbee.com?fpr=infrabench7552)**
* **[Rent Verified GPUs on Vast.ai →](https://cloud.vast.ai/?ref_id=749467)**
* **[FastSEOHub Search & Indexing Tool →](https://www.digistore24.com/redir/676823/infrabench7552/)**
* **[n8n Self-Hosted Workflow Guide →](https://www.checkout-ds24.com/redir/667670/infrabench7552/)**

---

## License
MIT
