# Quick GPU Memory Cheat Sheet (and Cheapest Hourly GPUs Right Now)

I kept running into out-of-memory crashes whenever I turned up the context window on rented GPUs, so I wrote down the real memory numbers (model weights + context cache + safety buffer) and put together a free calculator here:

👉 **Live Calculator:** [https://sectoroneventures.github.io/infrabench/](https://sectoroneventures.github.io/infrabench/)

---

## Real GPU Memory Needed (at 32k Context Window)

| Model Size | 4-bit (AWQ / Q4) Memory | 8-bit (FP8) Memory | Best Cheap GPU Setup | Current Hourly Price |
| :--- | :--- | :--- | :--- | :--- |
| **8B** (Llama 3.1 / Qwen 2.5) | ~8.5 GB | ~12.5 GB | 1x RTX 3090 (24GB) | **$0.21/hr** |
| **14B** (Qwen 2.5 / Phi-4) | ~12.8 GB | ~19.4 GB | 1x RTX 3090 (24GB) | **$0.21/hr** |
| **32B** (DeepSeek-R1 / Qwen Coder) | ~22.4 GB | ~38.0 GB | 1x RTX 4090 (24GB) or 1x RTX 5090 (32GB) | **$0.62/hr – $0.89/hr** |
| **70B** (Llama 3.3 / DeepSeek-R1 70B) | ~46.8 GB | ~78.2 GB | 1x L40S (48GB) or 2x RTX 4090 (48GB) | **$0.54/hr** |
| **123B** (Mistral Large 2) | ~76.0 GB | ~138.0 GB | 1x A100 (80GB) or 2x L40S (96GB) | **$0.57/hr** |
| **671B** (DeepSeek-R1 Full) | ~412.0 GB | ~710.0 GB | 8x A100 (640GB) or 8x H100 | **$1.89/hr/GPU** |

---

## 1-Click Ready-to-Run Templates (on Vast.ai)

If you don't feel like setting up Docker flags and CUDA libraries from scratch, these templates start up ready to go:

* **[vLLM Server (FP8 Cache + AWQ Ready)](https://cloud.vast.ai/?ref_id=749467&template_id=f702973989cc33171c27cf3db6d5a545)**
* **[DeepSeek-R1 & Qwen 72B Fast SGLang Server](https://cloud.vast.ai/?ref_id=749467&template_id=5bdd3dd59970ee8c778a596bad88b6ee)**
* **[Ollama + Open WebUI Private Server (1-Click)](https://cloud.vast.ai/?ref_id=749467&template_id=a157e8865a334938872f9e1bbcc1573a)**
* **[Unsloth Fast Fine-Tuning Notebook (CUDA 12.8)](https://cloud.vast.ai/?ref_id=749467&template_id=2c8267748fc42b4cf6c75fe4200afb47)**
* **[ComfyUI Flux.1 Dev + Wan2.1 Video Studio](https://cloud.vast.ai/?ref_id=749467&template_id=a703d9051cbf75e7464128527f7bfe6d)**

Want to check a different context length or batch size? Use the free slider tool at **[sectoroneventures.github.io/infrabench](https://sectoroneventures.github.io/infrabench/)** or grab the Python script from **[GitHub](https://github.com/SectorOneVentures/infrabench)**.
