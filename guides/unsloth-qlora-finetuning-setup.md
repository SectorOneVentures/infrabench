# Fine-Tuning Models with Unsloth on a Cheap Rented GPU

If you're fine-tuning an 8B, 14B, or 70B model with QLoRA, **Unsloth** cuts memory usage in half and runs about 2x faster than standard Hugging Face `Trainer`.

## Which GPU Should You Rent?

* **For 8B or 14B QLoRA:** Grab a single **RTX 3090 (24GB)** for **$0.20/hr** or **RTX 4090 (24GB)** for **$0.44/hr**.
* **For 32B QLoRA:** Grab a **RTX 5090 (32GB)** for **$0.87/hr** or **L40S (48GB)** for **$0.60/hr**.
* **For 70B QLoRA:** Grab an **A100 80GB** for **$0.63/hr**.

---

## 1-Click Unsloth + JupyterLab Template

I saved a ready-to-use public template on Vast.ai with PyTorch 2.6, CUDA 12.8, and JupyterLab pre-configured on port `8080`:

👉 **[Launch Unsloth Fine-Tuning Template on Vast.ai](https://cloud.vast.ai/?ref_id=749467&template_id=2c8267748fc42b4cf6c75fe4200afb47)**

Check live GPU hourly prices and exact memory requirements before you spin up a box: **[https://sectoroneventures.github.io/infrabench/](https://sectoroneventures.github.io/infrabench/)**.
