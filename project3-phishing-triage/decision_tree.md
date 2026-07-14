# Phishing Triage Decision Tree

```
                     Incoming Suspicious Email
                                |
              -----------------------------------
              |                |                 |
           SAFE            SUSPICIOUS         MALICIOUS
     (0 red flags)      (1-2 red flags)   (3+ red flags OR
                                            dangerous attachment
                                            OR payment/credential
                                            request)
              |                |                 |
           CLOSE          WARN USER        BLOCK & ESCALATE
        No action.     Advise the user   Report to security
                        to verify via a   team immediately.
                        known, separate   Do not click/reply/
                        channel before    forward. Purge from
                        acting.           other inboxes.
```

## How to use this with the analyzer

1. Run `phishing_analyzer.py` against the email.
2. Read the printed **Risk score** and **Verdict**.
3. Cross-check the verdict against this tree and the `checklist.md`
   before taking action — the script is a first-pass aid, not a
   replacement for human judgment (see the false-positive note in
   the README).
