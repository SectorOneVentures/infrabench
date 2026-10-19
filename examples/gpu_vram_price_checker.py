#!/usr/bin/env python3
"""
Quick GPU Memory (VRAM) & Hourly Cloud Price Checker
Interactive Web Calculator: https://sectoroneventures.github.io/infrabench/
"""
import argparse

GPUS = [
    ("RTX 3090", 24, 0.19),
    ("RTX 4090", 24, 0.35),
    ("RTX 5090", 32, 0.67),
    ("L40S", 48, 0.46),
    ("A100 80GB", 80, 0.79),
    ("H100 80GB", 80, 1.93),
]

def check_vram(params_b: float, bits: float, ctx: int) -> None:
    weights_gb = params_b * (bits / 8.0) * 1.08
    kv_gb = (ctx / 4096.0) * (params_b / 7.0) * 0.45
    total_gb = round((weights_gb + kv_gb) * 1.10, 1)
    print(f"=== {params_b:g}B Model ({bits:g}-bit) @ {ctx:,} Context ===")
    print(f"Estimated VRAM Needed: {total_gb} GB (Weights: {weights_gb:.1f} GB + KV Cache: {kv_gb:.1f} GB)")
    for name, vram, price in GPUS:
        if vram >= total_gb:
            print(f"Fits on 1x {name} ({vram}GB) -> ~${price:.2f}/hr on Vast.ai: https://cloud.vast.ai/?ref_id=749467")
            break
    print("Interactive calculator & 1-click templates: https://sectoroneventures.github.io/infrabench/")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--params", type=float, default=32.0)
    p.add_argument("--bits", type=float, default=4.5)
    p.add_argument("--ctx", type=int, default=32768)
    args = p.parse_args()
    check_vram(args.params, args.bits, args.ctx)
