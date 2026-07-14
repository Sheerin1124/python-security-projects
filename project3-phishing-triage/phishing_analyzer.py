"""
Phishing Awareness Analyzer
----------------------------
DecodeLabs Cybersecurity Internship - Project 3

Reads a plain-text email (with headers) and flags common phishing
indicators, then classifies it as SAFE, SUSPICIOUS, or MALICIOUS
using a simple scoring model.

Usage:
    python phishing_analyzer.py sample_emails/suspicious_email.txt
"""

import re
import sys

# --- Red flag keyword banks -------------------------------------------------

URGENCY_WORDS = [
    "urgent", "immediately", "24 hours", "act now", "expires",
    "locked", "final notice", "verify now", "immediate action"
]

AUTHORITY_WORDS = [
    "ceo", "director", "hr", "it security", "law enforcement",
    "strictly confidential", "do not discuss"
]

BYPASS_WORDS = [
    "bypass", "do not discuss", "keep this confidential",
    "without approval", "skip the process"
]

DANGEROUS_EXTENSIONS = [".exe", ".scr", ".js", ".iso", ".vbs", ".bat", ".jar"]

SUSPICIOUS_URL_PATTERNS = [
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",   # raw IP address as a link
    r"-secure-", r"-login-", r"-update\.com", r"login-update",
]


def extract_field(text, field):
    match = re.search(rf"^{field}:\s*(.*)$", text, re.MULTILINE | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def check_domain_mismatch(from_field):
    """Flags when the display name suggests one org but the domain is another."""
    match = re.search(r"<([^>]+)>", from_field)
    if not match:
        return False
    domain = match.group(1).split("@")[-1].lower()
    trusted_domains = ["decodelabs.tech"]
    # Flag anything that ISN'T the trusted domain but looks like it's trying to be
    if domain not in trusted_domains and "decodelabs" in domain:
        return True  # lookalike / subdomain trap
    if domain not in trusted_domains and any(
        w in from_field.lower() for w in ["ceo", "it security", "hr", "support"]
    ):
        return True  # impersonating an internal role from an outside domain
    return False


def analyze_email(text):
    findings = []
    score = 0

    from_field = extract_field(text, "From")
    subject = extract_field(text, "Subject")
    body = text.lower()

    # 1. Sender/domain mismatch
    if check_domain_mismatch(from_field):
        findings.append("Sender display name does not match the actual domain "
                         f"(From: {from_field})")
        score += 3

    # 2. Urgency language
    hits = [w for w in URGENCY_WORDS if w in body or w in subject.lower()]
    if hits:
        findings.append(f"Urgency/pressure language detected: {', '.join(hits)}")
        score += 2

    # 3. Authority impersonation
    hits = [w for w in AUTHORITY_WORDS if w in body]
    if hits:
        findings.append(f"Authority impersonation cues: {', '.join(hits)}")
        score += 2

    # 4. Requests to bypass normal process / secrecy
    hits = [w for w in BYPASS_WORDS if w in body]
    if hits:
        findings.append(f"Requests to bypass process or keep it secret: {', '.join(hits)}")
        score += 3

    # 5. Dangerous attachment extensions
    for ext in DANGEROUS_EXTENSIONS:
        if ext in body:
            findings.append(f"Dangerous attachment extension found: {ext}")
            score += 4

    # 6. Suspicious links / lookalike domains
    for pattern in SUSPICIOUS_URL_PATTERNS:
        if re.search(pattern, body):
            findings.append(f"Suspicious link pattern matched: '{pattern}'")
            score += 3

    # --- Classification ---
    if score == 0:
        verdict = "SAFE"
        action = "Close - no action needed"
    elif score <= 4:
        verdict = "SUSPICIOUS"
        action = "Warn User - advise manual verification via a known channel"
    else:
        verdict = "MALICIOUS"
        action = "Block & Escalate - report to security team immediately"

    return {
        "from": from_field,
        "subject": subject,
        "score": score,
        "verdict": verdict,
        "action": action,
        "findings": findings,
    }


def print_report(result):
    print("=" * 60)
    print(f"From:    {result['from']}")
    print(f"Subject: {result['subject']}")
    print("-" * 60)
    if result["findings"]:
        print("Red flags found:")
        for i, f in enumerate(result["findings"], 1):
            print(f"  {i}. {f}")
    else:
        print("No red flags detected.")
    print("-" * 60)
    print(f"Risk score: {result['score']}")
    print(f"Verdict:    {result['verdict']}")
    print(f"Action:     {result['action']}")
    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python phishing_analyzer.py <path_to_email.txt>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        email_text = f.read()

    result = analyze_email(email_text)
    print_report(result)
