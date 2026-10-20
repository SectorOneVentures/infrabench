# Cheap Cloud GPU Setup for ComfyUI (Flux.1 Dev & Wan2.1 Video)

Running **Flux.1 Dev** or **Wan2.1 (14B video)** locally eats up 20GB to 30GB of VRAM pretty fast. If your home PC only has 8GB–12GB of VRAM, you don't need to pay $2+/hr on big cloud providers.

Here is what 24GB+ cards actually cost per hour on **[Vast.ai](https://cloud.vast.ai/?ref_id=749467)** right now:
* **RTX 3090 (24GB):** **$0.17/hr** — Good for Flux.1 Dev (FP8/NF4) and Wan2.1 1.3B/14B quantized
* **RTX 4090 (24GB):** **$0.54/hr** — Way faster step times for video generation
* **RTX 5090 (32GB):** **$0.60/hr** — Extra 8GB headroom so you don't hit out-of-memory errors when loading ControlNets + LoRAs
* **L40S (48GB):** **$0.60/hr** — Tons of room for unquantized FP16 workflows

---

## 1-Click ComfyUI Studio Template

Instead of installing PyTorch and custom nodes every time, you can boot straight into ComfyUI on CUDA 12.9 using this public template:

👉 **[Launch ComfyUI Flux.1 + Wan2.1 Template on Vast.ai](https://cloud.vast.ai/?ref_id=749467&template_id=a703d9051cbf75e7464128527f7bfe6d)**

And if you want to compare live GPU prices or check memory math first, I keep a live price table updated every 6 hours here: **[https://sectoroneventures.github.io/infrabench/](https://sectoroneventures.github.io/infrabench/)**.
