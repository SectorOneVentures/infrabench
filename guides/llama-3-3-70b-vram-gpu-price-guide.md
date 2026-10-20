# How Much GPU Memory You Need for Llama 3.3 70B (and Cheapest Hourly GPUs)

Running **Llama 3.3 70B Instruct** on rented cloud GPUs is way cheaper than paying per-token API bills once you run batch jobs — as long as you pick a card that fits the weights plus your context window.

👉 **Interactive VRAM & Price Calculator:** [https://sectoroneventures.github.io/infrabench/](https://sectoroneventures.github.io/infrabench/)

---

## Memory Needed at 32k Context Window

* **4-Bit Quantized (AWQ / GGUF Q4_K_M):** Needs **~46.8 GB VRAM** total.
  * **Cheapest single card:** Rent 1x **L40S (48GB)** on **[Vast.ai](https://cloud.vast.ai/?ref_id=749467)** for **$0.60/hr**.
  * **Cheapest dual-card setup:** Rent 2x **RTX 3090 (48GB total)** for ~**$0.38/hr** or 2x **RTX 4090 (48GB total)** for ~**$0.70/hr**.
* **8-Bit Quantized (FP8):** Needs **~78.2 GB VRAM** total.
  * **Best card:** Rent 1x **A100 80GB** on **[Vast.ai](https://cloud.vast.ai/?ref_id=749467)** for **$0.63/hr**.

### Launch in 1 Click
* **[1-Click vLLM Server on Vast.ai](https://cloud.vast.ai/?ref_id=749467&template_id=f702973989cc33171c27cf3db6d5a545)**
* **[1-Click Ollama + Open WebUI Server on Vast.ai](https://cloud.vast.ai/?ref_id=749467&template_id=a157e8865a334938872f9e1bbcc1573a)**
