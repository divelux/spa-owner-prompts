"""Checks prompts.json and prompts.md. Standard library only: python3 validate.py

- prompts.json parses and has the expected shape
- ids are unique kebab-case; every prompt has a title, use case, category and variables
- every {{variable}} in a prompt is declared, and every declared variable is used
- every prompt lists the three core guardrails and carries their text in its Rules block
- no banned wording anywhere in prompts.json or prompts.md: health claims ("detox", "cure",
  "burn fat", "heal" ...), hype ("clinically proven", "#1"), and anything about getting a
  sauna hat wet (hats are worn dry)
- prompts.md is in step with prompts.json

(c) 2026 DIVELUX Inc. MIT License. https://diveluxsaunahat.com
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = ["no-health-claims", "not-medical-advice", "no-invented-facts"]
ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
VAR = re.compile(r"\{\{(\w+)\}\}")

BANNED = [
    r"\bdetox\w*", r"\btoxin\w*", r"\bcure[sd]?\b", r"\bcuring\b", r"\bheal(s|ed|ing|er)?\b",
    r"\bburn\w*\s+(body\s+)?fat\b", r"\bfat[- ]burn\w*", r"\bweight[- ]loss\b", r"\blose weight\b",
    r"\bboost\w*\s+(your\s+)?immun\w*", r"\banti[- ]?aging\b", r"\bclinically\b", r"\bscientifically proven\b",
    r"\bmiracle\b", r"\bguarantee[sd]?\b", r"#1\b", r"\b(5|five)[- ]star\b",
    # sauna hats are worn dry
    r"\bwet\w*\b", r"\bsoak\w*", r"\bdamp\w*", r"\bmoisten\w*", r"\bwring\w*",
]
BANNED_RE = re.compile("|".join(BANNED), re.I)

problems = []


def check(cond, msg):
    if not cond:
        problems.append(msg)


def main():
    with open(os.path.join(HERE, "prompts.json"), encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)
    for key in ("name", "version", "license", "publisher", "system_prompt", "core_guardrails", "prompts"):
        check(key in data, "missing top-level key " + key)
    check("CC BY 4.0" in data.get("license", ""), "license must be CC BY 4.0")
    core = {g["id"]: g["text"] for g in data.get("core_guardrails", [])}
    check(sorted(core) == sorted(CORE), "core guardrails: %s" % sorted(core))
    check("not medical advice" in core.get("not-medical-advice", ""), "not-medical-advice text lacks the phrase")

    ids = set()
    prompts = data.get("prompts", [])
    check(len(prompts) >= 15, "expected at least 15 prompts, got %d" % len(prompts))
    for p in prompts:
        pid = p.get("id", "?")
        check(ID.match(pid or "") is not None, "bad id %r" % pid)
        check(pid not in ids, "duplicate id " + pid)
        ids.add(pid)
        for key in ("category", "title", "use_case", "prompt", "variables", "guardrails"):
            check(bool(p.get(key)), "%s: empty %s" % (pid, key))
        declared = [v["name"] for v in p.get("variables", [])]
        check(len(declared) == len(set(declared)), pid + ": duplicate variable")
        used = set(VAR.findall(p.get("prompt", "")))
        check(used == set(declared), "%s: used %s, declared %s" % (pid, sorted(used), sorted(declared)))
        for v in p.get("variables", []):
            check(isinstance(v.get("required"), bool) and v.get("description") and v.get("example"),
                  "%s: variable %s needs description, example, required" % (pid, v.get("name")))
        check(sorted(p.get("guardrails", [])) == sorted(CORE), pid + ": guardrails must be the three core ones")
        for gid in CORE:
            check(core.get(gid, "\0") in p.get("prompt", ""), "%s: Rules block lacks guardrail %s" % (pid, gid))
        check(len(p.get("prompt", "")) < 4000, pid + ": prompt is very long")
        check("venue_name" in declared, pid + ": every prompt should take venue_name")

    with open(os.path.join(HERE, "prompts.md"), encoding="utf-8") as f:
        md = f.read()
    for name, text in (("prompts.json", raw), ("prompts.md", md)):
        for m in BANNED_RE.finditer(text):
            a = max(0, m.start() - 40)
            problems.append("%s: banned wording %r in ...%s..." % (name, m.group(0), text[a:m.end() + 40].replace("\n", " ")))
    for p in prompts:
        check(p["prompt"] in md, p["id"] + ": prompts.md is out of date (run build.py)")
    check(md.count("\n### ") == len(prompts), "prompts.md heading count")
    check(md.count("\n# ") + md.startswith("# ") == 1, "prompts.md must have one H1")

    print("%d prompts, %d categories, %d variables" % (
        len(prompts), len({p["category"] for p in prompts}), sum(len(p["variables"]) for p in prompts)))
    if problems:
        print("PROBLEMS:\n  " + "\n  ".join(problems))
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
