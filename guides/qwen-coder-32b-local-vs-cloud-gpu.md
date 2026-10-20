# How Much GPU Memory You Actually Need for Qwen 2.5 Coder 32B

When you run a coding model with a 32,000-token context window, your graphics card memory (VRAM) gets used by two things:
1. **The weights:** The model itself (~18–20 GB for 4-bit, ~34 GB for 8-bit).
2. **The scratchpad (context cache):** Room to remember 32,000 tokens of your code files (~3–6 GB).

---

## 1. The 4-Bit Version (AWQ / Q4_K_M) — Best Value
* **Total VRAM needed (at 32k context):** ~**22.4 GB** (with FP8 cache turned on)
* **What card to rent:** Fits on a single **RTX 3090 (24GB)** for **$0.17/hr** or **RTX 4090 (24GB)** for **$0.42/hr**. If you want a bigger 64k context window without running out of memory, grab an **RTX 5090 (32GB)** for **$0.60/hr**.

## 2. The 8-Bit Version (FP8)
* **Total VRAM needed (at 32k context):** ~**38.0 GB**
* **What card to rent:** Doesn't fit on a single 24GB card. Grab a single **L40S (48GB)** for **$0.60/hr** or 2x RTX 4090.

---

## Launch in 1 Click
* **[1-Click vLLM Server (FP8 Cache + AWQ Ready)](https://cloud.vast.ai/?ref_id=749467&template_id=f702973989cc33171c27cf3db6d5a545)**
* **[1-Click Ollama Server](https://cloud.vast.ai/?ref_id=749467&template_id=a157e8865a334938872f9e1bbcc1573a)**
* **[Interactive GPU Memory Calculator](https://sectoroneventures.github.io/infrabench/qwen-coder-32b-gpu-guide.html)**
