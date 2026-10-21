# How to Run a Private Ollama + Open WebUI Server for $0.22/hr

If you want to test big models (like DeepSeek-R1 32B/70B, Qwen 2.5 Coder, or Llama 3.3) privately without buying a $2,000 graphics card or paying monthly subscriptions, renting an hourly GPU box is super cheap as long as you turn it off when you're done.

Right now on **[Vast.ai](https://cloud.vast.ai/?ref_id=749467)**:
* **RTX 3090 (24GB VRAM):** ~**$0.22/hr** (runs 8B, 14B, and 32B 4-bit models easily)
* **RTX 4090 (24GB VRAM):** ~**$0.51/hr** (almost twice as fast for coding models)
* **L40S (48GB VRAM):** ~**$0.80/hr** (fits 70B models on a single card without splitting across GPUs)

---

## Easiest Way: 1-Click Template

I made a public template on Vast.ai that already has `ollama/ollama:latest` configured with port `11434` open and persistent storage set up:

👉 **[Launch 1-Click Ollama Server on Vast.ai](https://cloud.vast.ai/?ref_id=749467&template_id=a157e8865a334938872f9e1bbcc1573a)**

Once the box starts up, open the terminal and pull whatever model you want:

```bash
ollama run deepseek-r1:32b
# or for coding:
ollama run qwen2.5-coder:32b
```

If you aren't sure how much GPU memory a model needs before you rent a card, check my free calculator here: **[https://sectoroneventures.github.io/infrabench/](https://sectoroneventures.github.io/infrabench/)**.
