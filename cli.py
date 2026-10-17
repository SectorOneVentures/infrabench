#!/usr/bin/env python3
"""
InfraBench CLI — Real-Time GPU VRAM Sizing & Cloud Cost Comparison Utility
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DATA_PATH = Path(__file__).resolve().parent / "data" / "live_benchmarks.json"


def compute_vram_gb(
    params_b: float,
    quant_bits: float = 4.5,
    layers: int = 80,
    kv_heads: int = 8,
    head_dim: int = 128,
    ctx_len: int = 32768,
    batch_size: int = 4,
    fp8_kv: bool = True,
) -> dict[str, float]:
    bytes_per_param = quant_bits / 8.0
    weights_gb = params_b * bytes_per_param * 1.04
    kv_bytes = 1.0 if fp8_kv else 2.0
    kv_cache_gb = (2 * layers * kv_heads * head_dim * ctx_len * batch_size * kv_bytes) / (1024**3)
    buffer_gb = max(2.0, weights_gb * 0.08)
    total_gb = weights_gb + kv_cache_gb + buffer_gb
    return {
        "weights_gb": round(weights_gb, 2),
        "kv_cache_gb": round(kv_cache_gb, 2),
        "buffer_gb": round(buffer_gb, 2),
        "total_gb": round(total_gb, 2),
    }


def load_benchmarks() -> dict[str, Any]:
    if DATA_PATH.exists():
        return json.loads(DATA_PATH.read_text(encoding="utf-8"))
    return {"gpu_benchmarks": [], "referral_links": {}}


def main() -> None:
    parser = argparse.ArgumentParser(description="InfraBench — GPU VRAM & Live Cloud Cost Calculator")
    parser.add_argument("--params", type=float, default=70.0, help="Model size in billions of parameters (default: 70)")
    parser.add_argument("--quant", type=float, default=4.5, help="Bits per parameter: 16 (FP16), 8 (FP8/INT8), 4.5 (INT4/AWQ)")
    parser.add_argument("--ctx", type=int, default=32768, help="Context window tokens (default: 32768)")
    parser.add_argument("--batch", type=int, default=4, help="Concurrent sequences (default: 4)")
    args = parser.parse_args()

    res = compute_vram_gb(params_b=args.params, quant_bits=args.quant, ctx_len=args.ctx, batch_size=args.batch)
    data = load_benchmarks()
    vast_link = data.get("referral_links", {}).get("vast_ai", "https://cloud.vast.ai/?ref_id=749467")

    print(f"=== InfraBench VRAM Footprint ({args.params:.0f}B @ {args.quant}-bit, {args.ctx} ctx, batch={args.batch}) ===")
    print(
        f"Total VRAM: {res['total_gb']:.1f} GB "
        f"(Weights: {res['weights_gb']:.1f} GB | KV Cache: {res['kv_cache_gb']:.1f} GB | Buffer: {res['buffer_gb']:.1f} GB)\n"
    )
    print(f"{'GPU Model':<16} {'Topology':<12} {'VRAM':<10} {'Vast.ai $/hr':<14} {'RunPod $/hr':<14} {'AWS $/hr':<12}")
    print("-" * 80)

    valid_counts = [1, 2, 4, 8]
    matches = []
    for g in data.get("gpu_benchmarks", []):
        needed = 8
        for c in valid_counts:
            if c * g["vram_gb"] >= res["total_gb"] * 1.03:
                needed = c
                break
        if needed * g["vram_gb"] >= res["total_gb"]:
            matches.append((g["vast_min_dph"] * needed, needed, g))

    matches.sort(key=lambda x: x[0])
    for vast_dph, needed, g in matches:
        tot_vram = int(round(needed * g["vram_gb"]))
        runpod_dph = g["runpod_dph"] * needed
        aws_dph = g["aws_dph"] * needed
        print(
            f"{g['gpu']:<16} {f'{needed}x GPU':<12} {f'{tot_vram} GB':<10} "
            f"${vast_dph:<13.2f} ${runpod_dph:<13.2f} ${aws_dph:<11.2f}"
        )
    print(f"\nDeploy lowest-cost verified GPU nodes: {vast_link}")


if __name__ == "__main__":
    main()
