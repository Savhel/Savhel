#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import os
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
LOGIN = os.environ.get("PROFILE_LOGIN", "Savhel")
OUT = Path(os.environ.get("PROFILE_ACTIVITY_OUTPUT", "assets/github-activity.svg"))

if not TOKEN:
    raise SystemExit("GH_TOKEN or GITHUB_TOKEN is required")

QUERY = r'''
query($login: String!) {
  user(login: $login) {
    login
    followers { totalCount }
    repositories(
      first: 100
      ownerAffiliations: OWNER
      privacy: PUBLIC
      isFork: false
      orderBy: {field: UPDATED_AT, direction: DESC}
    ) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges {
            size
            node { name color }
          }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      totalPullRequestReviewContributions
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            contributionCount
            date
            weekday
          }
        }
      }
    }
  }
}
'''

def graphql(query: str, variables: dict) -> dict:
    payload = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={
            "Authorization": f"bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "savhel-profile-activity-generator",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode())
    if data.get("errors"):
        raise RuntimeError(json.dumps(data["errors"], indent=2))
    return data["data"]

def fmt(n: int) -> str:
    return f"{n:,}".replace(",", " ")

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

data = graphql(QUERY, {"login": LOGIN})
user = data.get("user")
if not user:
    raise SystemExit(f"GitHub user {LOGIN!r} not found")

repos = user["repositories"]["nodes"]
stars = sum(r["stargazerCount"] or 0 for r in repos)
followers = user["followers"]["totalCount"]
public_repos = user["repositories"]["totalCount"]

cc = user["contributionsCollection"]
calendar = cc["contributionCalendar"]
total_contrib = calendar["totalContributions"]
commits = cc["totalCommitContributions"]
prs = cc["totalPullRequestContributions"]

weeks = calendar["weeks"]
days = [d for w in weeks for d in w["contributionDays"]]
max_count = max([d["contributionCount"] for d in days] or [1])

lang_sizes = Counter()
lang_colors = {}
for repo in repos:
    for edge in repo["languages"]["edges"]:
        name = edge["node"]["name"]
        lang_sizes[name] += edge["size"]
        if edge["node"].get("color"):
            lang_colors[name] = edge["node"]["color"]

top_langs = lang_sizes.most_common(6)
lang_total = sum(v for _, v in top_langs) or 1

monthly = defaultdict(int)
for d in days:
    monthly[d["date"][:7]] += d["contributionCount"]
month_keys = sorted(monthly)[-12:]
month_vals = [monthly[k] for k in month_keys]
if len(month_vals) < 12:
    month_vals = [0] * (12 - len(month_vals)) + month_vals

W, H = 1440, 500
parts = []
def add(s: str):
    parts.append(s)

add(f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="{W}" y2="{H}">
    <stop stop-color="#07101D"/>
    <stop offset="1" stop-color="#101A35"/>
  </linearGradient>
  <linearGradient id="accent" x1="0" y1="0" x2="{W}" y2="0">
    <stop stop-color="#22D3EE"/>
    <stop offset=".5" stop-color="#3B82F6"/>
    <stop offset="1" stop-color="#A855F7"/>
  </linearGradient>
  <filter id="glow">
    <feGaussianBlur stdDeviation="4" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <style>
    .h{{font-family:Inter,Segoe UI,Arial,sans-serif;font-weight:800;fill:#F8FAFC}}
    .s{{font-family:Inter,Segoe UI,Arial,sans-serif;fill:#CBD5E1}}
    .m{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:#94A3B8}}
    .k{{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:13px;font-weight:700;fill:#93C5FD;letter-spacing:1.2px}}
  </style>
</defs>
<rect width="{W}" height="{H}" rx="28" fill="url(#bg)"/>
<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="26.5" stroke="#FFFFFF" stroke-opacity=".06"/>
<text x="68" y="58" class="h" font-size="32">GitHub Engineering Activity</text>
<text x="68" y="87" class="s" font-size="16">Self-hosted profile telemetry • generated from GitHub's API</text>
<rect x="68" y="104" width="1304" height="3" rx="1.5" fill="url(#accent)" opacity=".85"/>
''')

metrics = [
    ("CONTRIBUTIONS", total_contrib),
    ("COMMITS", commits),
    ("PULL REQUESTS", prs),
    ("PUBLIC REPOS", public_repos),
    ("FOLLOWERS", followers),
    ("STARS", stars),
]
mx, my, mw, mh, gap = 68, 130, 198, 82, 18
for i, (label, value) in enumerate(metrics):
    x = mx + i * (mw + gap)
    add(f'''<g>
  <rect x="{x}" y="{my}" width="{mw}" height="{mh}" rx="17" fill="#0F172A" stroke="#FFFFFF" stroke-opacity=".08"/>
  <text x="{x+18}" y="{my+27}" class="k">{escape(label)}</text>
  <text x="{x+18}" y="{my+62}" class="h" font-size="27">{escape(fmt(int(value)))}</text>
</g>''')

hx, hy = 68, 255
cell, cg = 11, 3
max_weeks = min(53, len(weeks))
weeks_draw = weeks[-max_weeks:]
add(f'<text x="{hx}" y="{hy-20}" class="h" font-size="19">Contribution map</text>')
add(f'<text x="{hx+265}" y="{hy-20}" class="m" font-size="12">{escape(fmt(total_contrib))} contributions in the current GitHub contribution window</text>')

palette = ["#172033", "#12324A", "#0D5671", "#0EA5B7", "#22D3EE"]
for wi, week in enumerate(weeks_draw):
    for d in week["contributionDays"]:
        c = int(d["contributionCount"])
        if c <= 0:
            level = 0
        else:
            ratio = math.log1p(c) / math.log1p(max_count)
            level = clamp(int(math.ceil(ratio * 4)), 1, 4)
        x = hx + wi * (cell + cg)
        y = hy + int(d["weekday"]) * (cell + cg)
        add(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2.5" fill="{palette[level]}"/>')

heat_w = max_weeks * (cell + cg)
add(f'''<line x1="{hx}" y1="{hy-5}" x2="{hx}" y2="{hy+7*(cell+cg)-cg+5}" stroke="#A5F3FC" stroke-width="1.2" opacity=".55" filter="url(#glow)">
  <animate attributeName="x1" values="{hx};{hx+heat_w}" dur="12s" repeatCount="indefinite"/>
  <animate attributeName="x2" values="{hx};{hx+heat_w}" dur="12s" repeatCount="indefinite"/>
</line>''')

sx, sy, sw, sh = 895, 255, 210, 92
add(f'<text x="{sx}" y="{sy-20}" class="h" font-size="19">12-month pulse</text>')
if month_vals:
    vmax = max(month_vals) or 1
    pts = []
    for i, v in enumerate(month_vals):
        x = sx + i * sw / 11
        y = sy + sh - (v / vmax) * sh
        pts.append(f"{x:.1f},{y:.1f}")
    add(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#60A5FA" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    for p in pts:
        x, y = p.split(",")
        add(f'<circle cx="{x}" cy="{y}" r="3.2" fill="#22D3EE"/>')

lx, ly = 1145, 255
add(f'<text x="{lx}" y="{ly-20}" class="h" font-size="19">Top languages</text>')
barw = 225
curx = lx
for name, size in top_langs:
    frac = size / lang_total
    width = max(2, barw * frac)
    color = lang_colors.get(name, "#60A5FA")
    add(f'<rect x="{curx}" y="{ly}" width="{width:.1f}" height="9" rx="4.5" fill="{escape(color)}"/>')
    curx += width

yy = ly + 31
for name, size in top_langs:
    pct = 100 * size / lang_total
    color = lang_colors.get(name, "#60A5FA")
    add(f'<circle cx="{lx+5}" cy="{yy-4}" r="4.5" fill="{escape(color)}"/>')
    add(f'<text x="{lx+18}" y="{yy}" class="s" font-size="12">{escape(name)} {pct:.1f}%</text>')
    yy += 20

updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
add(f'''<line x1="68" y1="452" x2="1372" y2="452" stroke="#FFFFFF" stroke-opacity=".08"/>
<text x="68" y="478" class="m" font-size="11">DATA  api.github.com/graphql</text>
<text x="720" y="478" text-anchor="middle" class="m" font-size="11">PROFILE  @{escape(LOGIN)}</text>
<text x="1372" y="478" text-anchor="end" class="m" font-size="11">UPDATED  {escape(updated)}</text>
</svg>''')

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("".join(parts), encoding="utf-8")
print(f"Wrote {OUT}")
