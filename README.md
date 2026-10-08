# ZaidinCoffeeScraper

<p align="center">
  <img src="logo.png" alt="Logo del proyecto" width="300">
</p>

Tinny Cafés Zaidin / Soy Cafetera Coffee Scraper

This is not a serious project, just a scraper that helps me search for the cheapest to most expensive coffees our my favourite coffee roaster (with the process type).

This Python script uses [Playwright](https://playwright.dev/python/) to scrape coffee products from [soycafetera.es](https://www.soycafetera.es/tienda/). It extracts the product name, price, and coffee processing method, then sorts them by price per kilogram.

---

## 🚀 Features

- Headless scraping via Playwright (Chromium)
- Auto-detection of product packaging (250g, 500g, etc.)
- Smart price normalization to €/kg
- Process parsing from product pages
- Results ordered by price
- Automatically handles cookies and lazy-loaded pages

---

## 🧰 Requirements

- Python 3.11+
- [Playwright for Python](https://playwright.dev/python/)
- [dependency-injector](https://python-dependency-injector.ets-labs.org/)

Install dependencies:

```bash
uv init
uv add playwright dependency-injector
uv run playwright install
```

And run main:

```bash
uv run main.py
```

---

Finally, you can copy the terminal output into a Markdown file and view the result like this:

| Name | Price | Process |
| :----------------------------: | :----------: | :-------------: |
| **Colombia Las Taguas** | **27.00€/kg** | *Lavado* |
| **El espectáculo, the amazing blend** | **27.00€/kg** | *Unknown* |
| **Descafeinado Brasil Turquesa Arábica Natural CO2** | **28.00€/kg** | *Natural* |
| **Etiopía Sidamo Shantawene** | **28.00€/kg** | *Lavado* |
| **Brasil Caramelo** | **30.00€/kg** | *Natural* |
| **Descafeinado México Azteca Arábica Lavado Mountain Water** | **30.00€/kg** | *Mountain Water* |

## Status

This project is just for testing and educational purposes. It works for me, so I probably won’t fix the missing fields in the coffee descriptions.
