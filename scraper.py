#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SlipNet Collector - Scrapes SlipNet links from Telegram channels
Author: THE SAZ 🏴‍☠️
Repository: https://github.com/its-thesaz/slipnet-collector
"""

import re
import html
import requests
import time
from datetime import datetime, timedelta
from collections import OrderedDict
from zoneinfo import ZoneInfo

# ========== CONFIGURATION ==========
TEHRAN_TZ = ZoneInfo("Asia/Tehran")

CHANNELS = [
    "xgvpn",
    "npvtunel_karing_hiddify",
    "appxa",
    "RavenAzad",
    "slipnet11",
    "JavidanNet",
    "appxa2",
    "baraye_azadi_gp",
    "amir_webstudio",
    "IRAN_V2RAY1",
    "SlipNet_decode",
    "blackRay",
    "SparrK_VPN",
    "slipnet_chat",
    "SlipNet_app",
    "VConfing",
    "capcutchina"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://t.me/"
}

SLIPNET_REGEX = re.compile(r'slipnet(?:-enc)?:\/\/[^\s<>"\'\[\]{}|\\^`]+', re.IGNORECASE)

OUTPUT_FILE = "SAZ🏴‍☠️.TXT"

# ========== SESSION ==========
session = requests.Session()
session.headers.update(HEADERS)

# ========== FUNCTIONS ==========
def fetch_channel_page(username: str) -> str:
    """Fetch Telegram channel preview page with retry logic."""
    url = f"https://t.me/s/{username}"
    retries = 3
    backoff = 2
    
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=15)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            if attempt < retries - 1:
                print(f"[!] Warning: Connection to {username} failed. Retrying in {backoff}s... ({e})")
                time.sleep(backoff)
                backoff *= 2
            else:
                print(f"[!] Error fetching {username} after {retries} attempts: {e}")
    return ""

def clean_link(link: str) -> str:
    """Remove trailing garbage characters from extracted links."""
    link = link.strip()
    link = re.sub(r'[\s.\,;:\)\(\"\'<>]+$', '', link)
    return link

def extract_links_from_html(html_content: str) -> set:
    """Extract all SlipNet links from HTML content."""
    found_links = set()
    if not html_content:
        return found_links
    
    decoded_html = html.unescape(html_content)
    
    # Find links in text
    for match in SLIPNET_REGEX.findall(decoded_html):
        cleaned = clean_link(match)
        if cleaned:
            found_links.add(cleaned)
    
    # Find links in href attributes
    href_links = re.findall(r'href=["\'](slipnet(?:-enc)?:\/\/[^"\']+)["\']', decoded_html, re.IGNORECASE)
    for link in href_links:
        cleaned = clean_link(link)
        if cleaned:
            found_links.add(cleaned)
    
    return found_links

def get_next_refresh(minutes: int = 10) -> str:
    """Calculate next refresh time in Tehran timezone."""
    now_tehran = datetime.now(TEHRAN_TZ)
    future = now_tehran + timedelta(minutes=minutes)
    return future.strftime("%I:%M %p").lstrip("0")

def generate_output(per_channel_data: OrderedDict, total_unique: int) -> str:
    """Generate highly graphical output with decorative elements."""
    now_tehran = datetime.now(TEHRAN_TZ)
    now_str = now_tehran.strftime("%Y-%m-%d %H:%M:%S")
    next_refresh = get_next_refresh(10)

    lines = []
    
    # ===== TOP BORDER =====
    lines.append("  ╔══════════════════════════════════════════════════════════════════╗")
    lines.append("  ║  ✦  S L I P N E T   C O L L E C T O R  ✦  ")
    lines.append("  ╠══════════════════════════════════════════════════════════════════╣")
    lines.append(f"  ║  📅 Last update  : {now_str}")
    lines.append(f"  ║  📊 Total nodes  : {total_unique}")
    lines.append(f"  ║  🔄 Next refresh : {next_refresh}")
    lines.append("  ╚══════════════════════════════════════════════════════════════════╝")
    lines.append("")

    # ===== CHANNEL SECTIONS with borders =====
    for ch, links in per_channel_data.items():
        count = len(links)
        if count == 0:
            continue
        
        # Channel header with rounded corners
        lines.append(f"  ┌─── ◆ {ch} ◆ ─── ({count} node{'s' if count > 1 else ''}) ───┐")
        
        # Links with bullet points and alternating style
        for idx, link in enumerate(links):
            prefix = "  │  📡" if idx % 2 == 0 else "  │  🔗"
            lines.append(f"{prefix}  {link}")
        
        # Channel footer
        lines.append("  └" + "─" * 60 + "┘")
        lines.append("")

    # ===== FOOTER with ASCII art =====
    lines.append("  ╔══════════════════════════════════════════════════════════════════╗")
    lines.append("  ║  🏴‍☠️  OVERHAULED BY THE SAZ  🏴‍☠️")
    lines.append("  ╠══════════════════════════════════════════════════════════════════╣")
    lines.append("  ║")
    lines.append("  ║    ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄")
    lines.append("  ║   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌")
    lines.append("  ║   ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌")
    lines.append("  ║   ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌")
    lines.append("  ║   ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌")
    lines.append("  ║   ▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌")
    lines.append("  ║   ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌")
    lines.append("  ║   ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌")
    lines.append("  ║   ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌")
    lines.append("  ║   ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌")
    lines.append("  ║    ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀")
    lines.append("  ║")
    lines.append("  ║  🏴‍☠️  THE SAZ  🏴‍☠️")
    lines.append("  ║")
    lines.append("  ║  🔗  More: t.me/the_saz")
    lines.append("  ║  🌐  Repo: github.com/its-thesaz/slipnet-collector")
    lines.append("  ╚══════════════════════════════════════════════════════════════════╝")

    return "\n".join(lines)

def main():
    """Main execution function."""
    print(f"[{datetime.now(TEHRAN_TZ).isoformat()}] Starting SlipNet collector (TXT mode)")

    per_channel_links = OrderedDict()
    all_unique_links = set()

    for ch in CHANNELS:
        print(f"  -> Fetching {ch}")
        html_content = fetch_channel_page(ch)
        if not html_content:
            per_channel_links[ch] = []
            continue

        links = extract_links_from_html(html_content)
        if not links:
            per_channel_links[ch] = []
            print(f"      No slipnet links found")
        else:
            unique_links = list(links)
            per_channel_links[ch] = unique_links
            all_unique_links.update(unique_links)
            print(f"      Found {len(unique_links)} unique slipnet link(s)")

        time.sleep(1.5)

    total_unique_all = len(all_unique_links)
    print(f"Total unique configs (across all channels): {total_unique_all}")

    output_content = generate_output(per_channel_links, total_unique_all)

    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(output_content)
        print(f"✅ Output successfully saved to {OUTPUT_FILE}")
    except Exception as e:
        print(f"[!] Error saving output file: {e}")

if __name__ == "__main__":
    main()