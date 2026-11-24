#!/usr/bin/env python3
"""One Emoji, One Smile — write exactly one emoji to /output/entry.txt.

The judge compares entries two at a time and picks the one more likely to
make a stranger smile, weighing in order:
  1. a single emoji that plainly aims to warm a stranger,
  2. warmth at first glance, no context needed,
  3. universality — no irony or in-joke that could land wrong,
  4. chosen rather than default, while staying instantly readable,
  5. right for a stranger — no intimacy, sarcasm or flirtation.

Head-to-head weighing (judge's ordered criteria):
  - U+1F60A (default smiling face): warm, but it is the first smiley that
    comes to mind — criterion 4 punishes exactly that, and it is the most
    likely house anchor text (a byte-identical copy never enters the playoff).
  - U+1F970 (smiling face with hearts, pass 1): ties the winner on warmth,
    universality and chosen-ness, but its hearts signal affection — from a
    stranger that can read as intimacy or flirtation, so it loses on
    criterion 5.
  - U+1F642 (slightly smiling face): reads as irony or passive-aggression
    to many people — fails universality (criterion 3).
  - U+1F33B (sunflower) and U+1F436 (dog face): cheerful and cute, but
    neither reads directly as a warm, friendly greeting — they lose on
    criteria 1 and 2.

Final pick: U+1F917 HUGGING FACE. A smiling face with open hands offering a
welcome: plainly warm at first glance, read the same way by any age or
background, clearly chosen rather than the default smiley, and friendly
without a trace of romance, sarcasm or intimacy — right for a stranger.
"""

import os

EMOJI = "\U0001F917"  # hugging face

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(EMOJI)
