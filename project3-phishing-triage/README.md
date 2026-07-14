# Project 3: Phishing Awareness Analysis

DecodeLabs Cybersecurity Internship — Defensive Logic Track
Batch 2026

## Goal
Analyze sample emails to identify phishing attempts: flag suspicious
links/keywords, list red flags, and explain why each message is
unsafe — using both a manual checklist and a small Python script.

## What's in this folder

```
project3-phishing-triage/
├── phishing_analyzer.py      # Script that scores an email and flags red flags
├── checklist.md               # Non-expert triage checklist
├── decision_tree.md           # Safe / Suspicious / Malicious decision tree
├── sample_emails/
│   ├── safe_email.txt
│   ├── suspicious_email.txt
│   └── malicious_email.txt
└── README.md
```

## Requirements
- Python 3.8+ (check with `python3 --version`)
- No external libraries needed — uses only the Python standard library.

## How to run it

1. Open the folder in VS Code (`File > Open Folder`).
2. Open a terminal in VS Code (`` Ctrl+` `` or `View > Terminal`).
3. Run the analyzer against any sample email:

```bash
python3 phishing_analyzer.py sample_emails/malicious_email.txt
python3 phishing_analyzer.py sample_emails/suspicious_email.txt
python3 phishing_analyzer.py sample_emails/safe_email.txt
```

Each run prints the sender, subject, red flags found, a numeric risk
score, and a verdict (SAFE / SUSPICIOUS / MALICIOUS) with a
recommended action.

## Findings / Writeup (for your submission)

- **malicious_email.txt** — Impersonates the CEO from an external
  domain (`executive-update.com`), uses urgency + secrecy + authority
  simultaneously, requests bypassing finance approval, and carries a
  `.iso` attachment. Score 17 → MALICIOUS → Block & Escalate.
- **suspicious_email.txt** — Sender domain (`decodelabs-secure-login.com`)
  is a lookalike of the real company domain, uses urgency language,
  and the link buries a fake domain behind a `decodelabs.tech` looking
  subdomain. Score 16 → MALICIOUS → Block & Escalate (this shows how
  even "moderate" looking phishing can score high once the domain
  mismatch is caught).
- **safe_email.txt** — Legitimate internal sender, no bypass or
  payment requests, no suspicious links. Note: the script flagged it
  SUSPICIOUS because "non-urgent" and "no immediate action" contain
  the substrings "urgent"/"immediate action." This is a known
  limitation of simple keyword matching — a good discussion point on
  why human review still matters alongside automated tools.

## Git workflow — pushing this to `python-security-projects`

If you haven't cloned your repo locally yet:
```bash
git clone https://github.com/Sheerin1124/python-security-projects.git
cd python-security-projects
```

Copy this folder into your repo, then:
```bash
git add project3-phishing-triage/
git commit -m "Add Project 3: Phishing Awareness Analysis"
git push origin main
```

If git asks for identity the first time on this machine:
```bash
git config --global user.name "Sheerin1124"
git config --global user.email "your-github-email@example.com"
```

If you're using GitHub Desktop instead of the terminal: drag the
`project3-phishing-triage` folder into your repo folder, it will show
up as new changes — write the same commit message and click
**Commit to main**, then **Push origin**.
