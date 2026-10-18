# Cheapest Way to Scrape Google Maps Business Leads (10k to 500k Places)

If you're pulling local business leads (phone numbers, websites, ratings, and reviews) from Google Maps, running your own Playwright script hits infinite-scroll memory leaks and IP blocks after a few hundred listings.

You can check the exact monthly math for your page volume on the free calculator here:

👉 **Interactive Scraper Cost Calculator:** [https://sectoroneventures.github.io/infrabench/headless-scraper-benchmark.html](https://sectoroneventures.github.io/infrabench/headless-scraper-benchmark.html)

---

## Real Cost for 10,000 Google Maps Listings

| Method | Setup Time | Proxy Cost Included? | Cost per 10k Places | Best Link |
| :--- | :--- | :--- | :--- | :--- |
| **[Apify Google Maps Scraper](https://apify.com?fpr=infrabench7552)** | 2 minutes (no code) | Yes (built-in) | **~$4.50 – $6.00** (first $5/mo is free) | **[Run on Apify Free →](https://apify.com?fpr=infrabench7552)** |
| **[ScrapingBee API](https://www.scrapingbee.com?fpr=infrabench7552)** | 15 minutes (Python/JS) | Yes (stealth proxies) | **~$6.80** (1,000 free calls) | **[Try ScrapingBee →](https://www.scrapingbee.com?fpr=infrabench7552)** |
| **Self-Hosted Playwright on [Vast.ai](https://cloud.vast.ai/?ref_id=749467)** | 2+ hours (Docker) | No (need residential IPs) | **~$4.80** ($0.17/hr server + proxy bandwidth) | **[Rent Linux Box →](https://cloud.vast.ai/?ref_id=749467)** |

---

## Quick Rule of Thumb
* **Under 50,000 places/month:** Use **[Apify](https://apify.com?fpr=infrabench7552)** — the free $5 monthly credit covers thousands of listings right out of the box without writing a single selector.
* **Custom HTML parsing across multiple directory sites:** Use **[ScrapingBee](https://www.scrapingbee.com?fpr=infrabench7552)** so you don't have to maintain proxy rotation.
* **Cleaning & categorizing leads with a local model:** Spin up a **$0.19/hr RTX 3090** on **[Vast.ai](https://cloud.vast.ai/?ref_id=749467&template_id=a157e8865a334938872f9e1bbcc1573a)** running Ollama to enrich the scraped JSON for pennies.
