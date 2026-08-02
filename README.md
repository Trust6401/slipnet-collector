# 🏴‍☠️ SlipNet Collector

> **The Ultimate SlipNet Link Aggregator**  
> *Collects, validates, and visualizes SlipNet VPN configurations from Telegram channels — automatically, every 10 minutes.*

<p align="center">
  <img src="https://img.shields.io/badge/version-3.0-blue?style=for-the-badge&logo=github" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/GitHub_Actions-Auto--deploy-2088FF?style=for-the-badge&logo=github-actions" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Web_Dashboard-Neon_UI-ff2d95?style=for-the-badge&logo=html5" alt="Dashboard">
  <img src="https://img.shields.io/badge/Developed_by-THE_SAZ-f1c40f?style=for-the-badge&logo=telegram" alt="Developer">
</p>

---

## ✦ Overview

**SlipNet Collector** is a fully automated tool that scrapes **SlipNet** and **SlipNet-Enc** links from 17+ public Telegram channels, compiles them into a beautifully formatted text file, and presents them through a **smart, neon-themed web dashboard** with real‑time validation, filtering, sorting, and auto‑refresh.

> 🔹 All you need is a GitHub repository — the entire system runs for free using **GitHub Actions** and **GitHub Pages**.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **🔄 Automated Scraping** | Runs every 10 minutes via GitHub Actions, fetches links from predefined Telegram channels |
| **📄 Graphically Rich Output** | The generated `SAZ🏴‍☠️.TXT` uses Unicode borders, emojis, and channel separators for a visually appealing result |
| **💻 Neon Web Dashboard** | A fully responsive, dark/light theme dashboard with neon glow effects and smooth animations |
| **🔍 Smart Filtering** | Search by link, filter by channel or status (Valid/Invalid/Pending) |
| **📊 Live Statistics** | Total nodes, validity ratio, and a mini progress chart |
| **✅ Real‑time Validation** | Validate each link’s format with a single click or validate all at once in parallel |
| **📌 Pagination & Sorting** | Sort by channel, link, or status; choose items per page (20/50/100/All) |
| **🌐 Multi‑language** | English and Persian (فارسی) with full RTL support — switch instantly |
| **⚡ Auto‑Refresh** | Set a custom interval (0–30 minutes) to automatically reload data |
| **📥 Export Data** | Download filtered nodes as JSON, CSV, or plain TXT |
| **🎨 Fully Customizable** | Font size, UI density, show/hide columns, and default sort — all saved in your browser |
| **📱 Mobile‑Optimized** | Perfectly responsive for any device |

---

## 🗂 Repository Structure

```
.
├── .github/workflows/main.yml   # GitHub Actions workflow (auto‑run every 10 min)
├── scraper.py                   # Python collector script
├── SAZ🏴‍☠️.TXT                  # Generated output file (auto‑committed)
├── index.html                   # Smart web dashboard (neon UI)
└── README.md                    # This file
```

---

## 🚀 How It Works

1. **Collector Script (`scraper.py`)**  
   - Fetches HTML previews of each Telegram channel (`t.me/s/...`).  
   - Extracts all `slipnet://` and `slipnet-enc://` links using regex.  
   - Formats the output with decorative borders, emojis, and channel sections.  
   - Saves everything into `SAZ🏴‍☠️.TXT`.

2. **GitHub Actions Workflow (`.github/workflows/main.yml`)**  
   - Triggered by schedule (`*/10 * * * *`) or manually via `workflow_dispatch`.  
   - Installs Python dependencies, runs `scraper.py`, and commits the updated file back to the repository.

3. **Web Dashboard (`index.html`)**  
   - Fetches `SAZ🏴‍☠️.TXT` from the repository’s raw URL.  
   - Parses and displays links with full interactivity:  
     - Filter by channel, status, or search term.  
     - Sort columns and paginate results.  
     - Validate links (format checking).  
     - Export filtered data.  
     - Switch languages, themes, font sizes, and density.  
   - Auto‑refresh keeps data up‑to‑date.

---

## 🛠 Setup & Usage

### Prerequisites
- A **GitHub account** (free tier is sufficient).
- A repository (public or private — public is needed for GitHub Pages).

### Step‑by‑Step

1. **Clone or create** a repository on GitHub.  
2. **Add the files** from this project into your repository:  
   - `.github/workflows/main.yml`  
   - `scraper.py`  
   - `index.html`  
3. **Update `REPO_OWNER` and `REPO_NAME`** inside `index.html` (lines ~800) to match your repository.  
4. **Enable GitHub Pages** for your repository (Settings → Pages → Branch: `main`).  
5. **Commit and push** the changes.  
6. **Wait** for the first workflow run (or trigger it manually from Actions tab).  

That’s it! Your dashboard will be available at:  
`https://<your-username>.github.io/<your-repo>/`

---

## 🧠 Configuration (Optional)

You can customize the list of Telegram channels inside `scraper.py` by modifying the `CHANNELS` array:

```python
CHANNELS = [
    "xgvpn",
    "npvtunel_karing_hiddify",
    # ... add or remove channels
]
```

All other settings (theme, language, refresh interval, etc.) are managed directly from the dashboard’s **Settings** panel and saved locally in your browser.

---

## 🖥 Dashboard Preview

<p align="center">
  <img src="https://img.shields.io/badge/Neon-UI-00d4ff?style=for-the-badge&logo=neon" alt="Neon UI">
  <img src="https://img.shields.io/badge/Responsive-Mobile Ready-39ff14?style=for-the-badge&logo=responsive" alt="Responsive">
</p>

The dashboard features:

- ✦ **Live node count** with validity percentages  
- ✦ **Mini chart** showing valid/pending/invalid ratios  
- ✦ **Quick actions**: Validate All, Download (JSON/CSV/TXT), Refresh  
- ✦ **Settings panel** with:  
  - Language (English / فارسی)  
  - Theme (Dark / Light)  
  - Font size (Small / Medium / Large)  
  - Density (Compact / Comfortable / Spacious)  
  - Show/Hide columns (Status, Channel)  
  - Auto‑validate on load  
  - Default sort column  
  - Items per page  
  - Auto‑refresh interval (minutes)  

All settings are persistent thanks to `localStorage`.

---

## 🔧 Technical Details

- **Python 3.10** + `requests` + `tzdata`  
- **GitHub Actions** for scheduling and auto‑committing  
- **Pure HTML/CSS/JS** frontend with zero external dependencies (except Font Awesome and Vazirmatn font)  
- **Neon theme** with CSS variables for easy theming  
- **RTL support** for Persian language  
- **Event delegation** and robust error handling for maximum stability

---

## 🧪 Validation Logic

Each link is tested against the regex:

```regex
^slipnet(?:-enc)?:\/\/[^\s<>"\'\[\]{}|\\^`]+$
```

Links that pass are marked **✅ Valid**, others **❌ Invalid**, and unvalidated ones appear as **⏳ Pending**.

---

## 👨‍💻 Developer

**THE SAZ** 🏴‍☠️

- Telegram: [@the_saz](https://t.me/the_saz)  
- GitHub: [its-thesaz](https://github.com/its-thesaz)

> *Built with passion, precision, and a neon touch.*

---

## 📜 License

This project is open‑source and available under the **APGL v3 License** (see [LICENSE](LICENSE) file for details).

---

## 🙌 Acknowledgments

- SlipNet community  
- All Telegram channels that share configurations  
- Vazirmatn font creators  
- Font Awesome icons  

---

## ⭐ Support

If you find this tool useful, please **star** the repository and share it with others.  
Contributions, suggestions, and feedback are always welcome!

---

<p align="center">
  <strong>Developed with 💜 by THE SAZ</strong><br>
  <sub>© 2026 • SlipNet Collector • Version 3.0</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/🚀-Always_Up--to--Date-ff6a00?style=for-the-badge" alt="Always Up-to-Date">
  <img src="https://img.shields.io/badge/⚡-Smart_Dashboard-39ff14?style=for-the-badge" alt="Smart Dashboard">
</p>
