#!/usr/bin/env python3
"""
Quick Monthly Web Scraping Cost Estimator (Apify vs. ScrapingBee vs. Self-Hosted Playwright)
Interactive Web Version: https://sectoroneventures.github.io/infrabench/headless-scraper-benchmark.html
Docker vs. Cloud TCO Calculator: https://sectoroneventures.github.io/infrabench/docker-vps-tco-estimator.html
"""
import argparse

def estimate(pages: int, js_ratio: float, stealth_ratio: float) -> None:
    # Base cost per 10k pages blended across static, JS, and stealth residential proxy tiers
    non_js = max(0.0, 1.0 - js_ratio - stealth_ratio)
    apify_10k = non_js * 1.35 + js_ratio * 5.20 + stealth_ratio * 14.90
    sbee_10k = non_js * 1.96 + js_ratio * 6.80 + stealth_ratio * 16.50
    vast_10k = non_js * 1.20 + js_ratio * 4.80 + stealth_ratio * 14.50

    scale = pages / 10000.0
    print(f"=== Monthly Cost Estimate for {pages:,} Pages ===")
    print(f"1. Apify Cloud Actors:       ${max(0.0, apify_10k * scale - 5.0):.2f}/mo (after $5/mo free credit)")
    print(f"   Try Free -> https://apify.com?fpr=infrabench7552")
    print(f"2. ScrapingBee Proxy API:    ${sbee_10k * scale:.2f}/mo (includes 1,000 free API calls)")
    print(f"   Try Free -> https://www.scrapingbee.com?fpr=infrabench7552")
    print(f"3. Vast.ai Playwright Box:   ${vast_10k * scale:.2f}/mo (starting at $0.19/hr RTX 3090 / Linux worker)")
    print(f"   Rent Box -> https://cloud.vast.ai/?ref_id=749467")
    print(f"\nFull interactive slider calculator: https://sectoroneventures.github.io/infrabench/headless-scraper-benchmark.html")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--pages", type=int, default=100000)
    p.add_argument("--js", type=float, default=0.5)
    p.add_argument("--stealth", type=float, default=0.2)
    args = p.parse_args()
    estimate(args.pages, args.js, args.stealth)
