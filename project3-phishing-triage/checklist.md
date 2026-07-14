# Phishing Triage Checklist (Non-Expert Friendly)

Use this checklist on any email that feels "off." You don't need
security training to run through this — just pause and check each box.

## 1. Sender
- [ ] Does the display name match the actual email address after the `@`?
- [ ] Is the domain spelled *exactly* right? (amaz0n.com, paypaI.com, etc. are fakes)
- [ ] Is this someone who would normally email me about this topic?

## 2. Tone
- [ ] Does it pressure me to act fast ("24 hours," "immediately," "account locked")?
- [ ] Does it invoke authority (CEO, IT, HR, "law enforcement")?
- [ ] Does it ask me to keep this secret or skip normal approval steps?

## 3. Links & Attachments
- [ ] Does hovering over the link show a different URL than the text?
- [ ] Is the "real" domain buried at the end of a long subdomain string?
      (e.g. `yourcompany.tech.login-update.com` — read right to left)
- [ ] Does the attachment have an unusual extension (.iso, .js, .scr, .exe)?
- [ ] Is there a QR code asking me to scan with my phone?

## 4. Request
- [ ] Is it asking for a password, MFA code, or payment details over email?
- [ ] Is it asking for a wire transfer or urgent payment?
- [ ] Am I getting repeated MFA push notifications I didn't request?

## Verdict
- **0 red flags** → Safe. Close it.
- **1–2 red flags** → Suspicious. Verify through a separate channel before acting.
- **3+ red flags, or any dangerous attachment/payment request** → Malicious.
  Block the sender and report to security. Do not click, reply, or forward.

## Golden Rule
**PAUSE → VERIFY → REPORT**
Never verify a suspicious request using contact info found *inside* the
suspicious message itself — always use a number/email you already knew
was legitimate before this email arrived.
