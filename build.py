"""Builds prompts.json and prompts.md from the definitions below. Standard library only.

    python3 build.py && python3 validate.py

Edit the prompts here, never the generated files.

(c) 2026 DIVELUX Inc. Code MIT; prompt texts CC BY 4.0. https://diveluxsaunahat.com
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
VERSION = "1.0.0"

# Every prompt carries these, written into its own Rules block so it works when copied alone.
CORE_GUARDRAILS = [
    ("no-health-claims",
     "Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or "
     "treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or "
     "immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body."),
    ("not-medical-advice",
     "If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add "
     "the sentence \"This is not medical advice; please talk to your doctor.\" and point to the house rules."),
    ("no-invented-facts",
     "Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest "
     "numbers, temperatures or any other figures or facts. Use only what is given above. Where something is "
     "missing, write [ASK OWNER: what is missing] instead of guessing."),
]

STYLE = ("Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, "
         "no emojis unless the owner asks for them.")

DISCLAIMER_LINE = "This is not medical advice; please talk to your doctor."

SYSTEM_PROMPT = (
    "You help the owner and staff of {{venue_name}}, a sauna, spa or bathhouse, write messages to guests, house "
    "rules, schedules and social media posts. " + STYLE + " Follow these rules in everything you write:\n"
    + "\n".join("- " + g for _, g in CORE_GUARDRAILS)
)

HAT_FACTS = (
    "Facts about sauna hats you may use: a sauna hat is a felt or wool hat worn in the hot room to keep heat off "
    "the head and ears. It is worn dry. If it is too big, fold up the brim or edge. Care for wool felt: hand wash "
    "only, in cool, room-temperature water (about 20–24 °C / 68–75 °F, never warm or hot), squeeze gently without "
    "twisting, and air dry; never a washing machine or a dryer."
)

PROMPTS = [
    # ---------------- guest replies
    {
        "id": "booking-reply",
        "category": "Guest replies",
        "title": "Reply to a booking question",
        "use_case": "A guest emails or messages to ask about times, availability or how to book.",
        "variables": [
            ("venue_name", "Name of your sauna, spa or club", "Cedar & Steam Sauna Club", True),
            ("guest_message", "The guest's message, pasted in full", "Hi, do you have space for 4 people Saturday afternoon?", True),
            ("booking_facts", "Hours, session lengths, how to book, group rules, anything true the reply may use", "Open Sat 9am-9pm. 2-hour sessions. Book at example.com/book. Groups of 4+ book a private room.", True),
            ("availability", "What you actually have free, or 'unknown'", "Private room free Sat 2-4pm", False),
        ],
        "body": (
            "You are replying for {{venue_name}}.\n\nGuest message:\n\"\"\"\n{{guest_message}}\n\"\"\"\n\n"
            "Facts you may use:\n{{booking_facts}}\n\nAvailability: {{availability}}\n\n"
            "Write a reply of 60 to 120 words. Answer exactly what was asked, give the next step to book, and stop. "
            "If availability is unknown, say a team member will confirm and do not promise a slot."
        ),
    },
    {
        "id": "first-visit-guide",
        "category": "Guest replies",
        "title": "What to expect on a first visit",
        "use_case": "Send to a guest who booked for the first time, or post as a page on your website.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("facilities", "Rooms and features, as they really are", "Wood-fired sauna, steam room, two cold plunges, garden lounge", True),
            ("session_format", "How a visit runs at your place", "Arrive 10 min early, 2-hour slot, showers before the hot room", True),
            ("provided", "What you provide and what guests bring", "Towels and robes provided. Bring swimwear and flip-flops.", True),
        ],
        "body": (
            "Write a friendly first-visit guide for {{venue_name}}.\n\nFacilities: {{facilities}}\n"
            "How a visit works: {{session_format}}\nWhat we provide / what to bring: {{provided}}\n\n"
            "Structure: Before you come; When you arrive; In the hot room; Cooling off; Leaving. "
            "Each part 2 to 4 short sentences. Tell first-timers they can sit on a lower bench, where it is cooler, "
            "and step out whenever they like. Do not give minutes or temperatures unless they are in the facts above."
        ),
    },
    {
        "id": "what-to-bring",
        "category": "Guest replies",
        "title": "What should I bring?",
        "use_case": "Quick answer to the most common pre-visit question, by message or email.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("provided", "What you provide", "Towels, robes, shampoo", True),
            ("required", "What guests must bring or wear", "Swimwear in mixed areas", True),
            ("optional", "Things guests may bring if they like", "Water bottle, flip-flops, a sauna hat", False),
            ("not_allowed", "What is not allowed", "Glass bottles, phones in the hot room", False),
        ],
        "body": (
            "Write a short packing list for a guest of {{venue_name}}, as a reply of under 100 words with a bullet list.\n\n"
            "We provide: {{provided}}\nGuests must bring: {{required}}\nOptional: {{optional}}\nNot allowed: {{not_allowed}}\n\n"
            "Only list items from the lines above. If a sauna hat is on the optional list, you may add one plain "
            "line about it. " + HAT_FACTS
        ),
    },
    {
        "id": "etiquette-reply",
        "category": "Guest replies",
        "title": "Answer an etiquette question",
        "use_case": "A guest asks about towels, talking, swimwear, phones, or how to behave in the hot room.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("guest_question", "The question", "Do I have to sit on a towel? Can I talk in the sauna?", True),
            ("house_rules", "Your actual house rules, pasted in", "Sit or lie on a towel. Quiet in the hot room. Shower first.", True),
        ],
        "body": (
            "Answer this guest question for {{venue_name}} in 40 to 90 words.\n\nQuestion: {{guest_question}}\n\n"
            "Our house rules:\n{{house_rules}}\n\n"
            "Base the answer on our rules only. Give the reason behind a rule in a few words where it helps "
            "(for example, a towel keeps the benches clean for the next guest). Be welcoming, never scolding."
        ),
    },
    {
        "id": "health-question-reply",
        "category": "Guest replies",
        "title": "A guest asks a health question",
        "use_case": "Pregnancy, heart, blood pressure, medication, an injury, or 'is sauna good for X?'. The reply must not advise.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("guest_message", "The guest's message", "I'm 20 weeks pregnant, is it OK to use the sauna?", True),
            ("house_policy", "What your rules say on this subject, if anything", "Guests with health conditions should check with their doctor before visiting.", True),
            ("alternatives", "Things you offer that do not involve heat, if any", "Garden lounge, tea bar", False),
        ],
        "body": (
            "Reply for {{venue_name}} to this message:\n\"\"\"\n{{guest_message}}\n\"\"\"\n\n"
            "Our policy: {{house_policy}}\nOther things we offer: {{alternatives}}\n\n"
            "Do not answer the medical question and do not say whether sauna is safe, good or bad for them. Thank "
            "them for asking, say we cannot give medical advice, ask them to check with their doctor, quote our "
            "policy, and mention the other things we offer if there are any. Under 90 words. Include the sentence: "
            "\"" + DISCLAIMER_LINE + "\""
        ),
    },
    {
        "id": "complaint-reply",
        "category": "Guest replies",
        "title": "Reply to a complaint",
        "use_case": "A guest complains in person, by email or in a public review.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("complaint", "The complaint, pasted in full", "The steam room was cold and nobody at the desk cared.", True),
            ("what_happened", "What you know happened, from your side", "Steam generator fault on Sunday, fixed Monday.", False),
            ("offer", "What you are willing to offer, or 'none'", "A free return visit", True),
            ("channel", "Where the reply goes: email, message, or public review", "public review", True),
        ],
        "body": (
            "Write a reply from {{venue_name}} to this complaint, for a {{channel}}.\n\nComplaint:\n\"\"\"\n{{complaint}}\n\"\"\"\n\n"
            "What we know: {{what_happened}}\nWhat we can offer: {{offer}}\n\n"
            "Thank them, own what went wrong without excuses, say what was done about it (only from 'what we know'), "
            "and make only the offer given above. If the offer is 'none', invite them to contact us directly. "
            "For a public review, keep it under 80 words and leave out personal details and booking numbers."
        ),
    },
    {
        "id": "review-thanks",
        "category": "Guest replies",
        "title": "Thank a guest for a good review",
        "use_case": "Reply to a positive public review without sounding copy-pasted.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("review", "The review text", "Loved the Aufguss with the eucalyptus, the host was great.", True),
            ("staff_names", "Staff the guest named, if they agree to be named back", "Mia", False),
        ],
        "body": (
            "Write a 30 to 60 word reply from {{venue_name}} to this review:\n\"\"\"\n{{review}}\n\"\"\"\n\n"
            "Staff we may name: {{staff_names}}\n\n"
            "Pick up one specific detail from the review. Do not repeat the guest's praise back as a quote, do not "
            "add a sales pitch, and do not mention offers."
        ),
    },
    # ---------------- rules and signs
    {
        "id": "house-rules",
        "category": "House rules and signs",
        "title": "Turn your notes into house rules",
        "use_case": "You have a messy list of rules; you want a clean page for the website, the wall or the booking email.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("rule_notes", "Your rules in any form", "shower first; towel under you; no phones in hot rooms; quiet; under 16 with adult; no alcohol", True),
            ("tone", "How it should sound", "friendly but clear", False),
        ],
        "body": (
            "Turn these notes into the house rules of {{venue_name}}.\n\nNotes:\n{{rule_notes}}\n\nTone: {{tone}}\n\n"
            "Group them under short headings (Before you go in; In the hot rooms; Cooling off; Looking after each "
            "other). One line per rule, starting with a verb. Keep every rule from the notes and add no new rules. "
            "Where a rule touches health or alcohol, end the page with: \"" + DISCLAIMER_LINE + "\""
        ),
    },
    {
        "id": "safety-signs",
        "category": "House rules and signs",
        "title": "Short safety signs",
        "use_case": "Text for small printed signs by the hot room, the plunge pool or the showers.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("locations", "Where the signs go", "sauna door, cold plunge, steam room", True),
            ("rules_for_signs", "The rules each sign must carry, from your house rules", "Step out if you feel dizzy. One person in the plunge at a time.", True),
        ],
        "body": (
            "Write sign text for {{venue_name}}, one sign per place: {{locations}}.\n\n"
            "Rules to use: {{rules_for_signs}}\n\n"
            "Each sign: a heading of 2 to 4 words and at most 3 short lines. Use only the rules above. Plain words a "
            "tired guest can read from two steps away. No times, temperatures or limits unless they are in the rules."
        ),
    },
    {
        "id": "hat-and-headwear-faq",
        "category": "House rules and signs",
        "title": "Sauna hat and headwear FAQ",
        "use_case": "Guests ask why people wear hats in the sauna, whether they can bring one, or how to care for it.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("hat_policy", "Your policy: allowed, sold at the desk, provided, or not allowed", "Guests may bring their own; we sell wool hats at the desk.", True),
        ],
        "body": (
            "Write a short FAQ (3 to 5 questions) about sauna hats for guests of {{venue_name}}.\n\n"
            "Our policy: {{hat_policy}}\n\n" + HAT_FACTS + "\n\n"
            "Use only these facts and our policy. Do not claim a hat prevents any harm or does anything for health "
            "or hair; say it keeps the head and ears more comfortable in the heat, which is why many people like one."
        ),
    },
    # ---------------- Aufguss
    {
        "id": "aufguss-schedule",
        "category": "Aufguss and events",
        "title": "Build a weekly Aufguss schedule",
        "use_case": "Turn sauna masters' availability and room times into a clean timetable for the wall and the website.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("rooms", "Rooms that host Aufguss", "Main sauna (seats 20)", True),
            ("hours", "Opening hours by day", "Mon closed; Tue-Fri 4pm-10pm; Sat-Sun 10am-10pm", True),
            ("hosts", "Sauna masters and when each one works", "Mia: Tue, Thu, Sat; Jon: Wed, Fri, Sun", True),
            ("session_rules", "Your own rules: session length, gap between sessions, first and last start, sessions per day", "15 min sessions, at least 45 min apart, first at opening +1h, last 1h before close", True),
            ("themes", "Scents or themes you actually have", "Eucalyptus, birch, citrus, music night on Fri", False),
        ],
        "body": (
            "Make a weekly Aufguss schedule for {{venue_name}}.\n\nRooms: {{rooms}}\nHours: {{hours}}\n"
            "Sauna masters: {{hosts}}\nOur session rules: {{session_rules}}\nThemes we have: {{themes}}\n\n"
            "Output a table with columns Day, Time, Room, Host, Theme. Follow our session rules exactly; never put "
            "two sessions in one room at the same time or a host on a day they do not work. Leave a day empty if "
            "nobody works it. After the table, list any rule you could not meet and why. Describe themes by scent "
            "and mood only."
        ),
    },
    {
        "id": "aufguss-intro-script",
        "category": "Aufguss and events",
        "title": "Sauna master's opening words",
        "use_case": "A short spoken introduction before an Aufguss: welcome, what will happen, how to leave.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("host_name", "The sauna master", "Mia", True),
            ("theme", "Scent or theme of this session", "Birch and pine", True),
            ("rounds", "How many pours and fans you will do", "three", True),
        ],
        "body": (
            "Write what {{host_name}} says before an Aufguss at {{venue_name}}: 60 to 100 words, easy to say aloud.\n\n"
            "Theme: {{theme}}\nRounds of pouring and fanning: {{rounds}}\n\n"
            "Include: a welcome; that an Aufguss is water, here with {{theme}}, poured on the hot stones and the "
            "air fanned with a towel; that the heat rises in waves; that the lower benches are cooler; and that "
            "anyone may leave at any time, quietly, and should step out if they feel dizzy or unwell."
        ),
    },
    {
        "id": "event-announcement",
        "category": "Aufguss and events",
        "title": "Announce a special event",
        "use_case": "A sauna night, a guest sauna master, a holiday schedule or a members' evening.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("event_facts", "Date, time, what happens, price, how to book, capacity", "Fri Dec 5, 7-10pm, candlelight Aufguss with guest host. $45, book at example.com/events. 30 places.", True),
            ("channel", "Where it goes: email, Instagram, website, poster", "email", True),
        ],
        "body": (
            "Write an announcement for {{venue_name}} for {{channel}}.\n\nEvent facts:\n{{event_facts}}\n\n"
            "Lead with what and when, then what guests will experience, then how to book. Use only the facts given: "
            "no invented prices, places left, countdowns or 'selling fast'. For email, add a subject line under 50 "
            "characters. For a poster, keep it under 40 words."
        ),
    },
    # ---------------- social media
    {
        "id": "social-week-plan",
        "category": "Social media",
        "title": "A week of social posts",
        "use_case": "Plan five posts for the coming week from what is really happening at your venue.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("this_week", "What is on this week and anything new", "New birch whisks in; Thu music Aufguss; holiday hours Dec 24-26", True),
            ("platforms", "Where you post", "Instagram, Facebook", True),
            ("photos", "Photos you have (describe them)", "Steam on stones; empty sauna at dawn; staff tying whisks", False),
        ],
        "body": (
            "Plan 5 posts for {{venue_name}} on {{platforms}} for this week.\n\nThis week: {{this_week}}\n"
            "Photos we have: {{photos}}\n\n"
            "For each post: day, photo to use (from the list, or 'needs photo'), caption of 40 to 90 words, and at "
            "most 5 hashtags. Mix: one practical (hours, booking), one about the ritual or craft, one about people "
            "or staff, one event, one quiet atmosphere post. Only mention people in photos if the owner confirms "
            "they agreed to be posted."
        ),
    },
    {
        "id": "photo-caption",
        "category": "Social media",
        "title": "Caption and alt text for one photo",
        "use_case": "You have one photo and want a caption plus a description for people using screen readers.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("photo_description", "What is in the photo", "Ladle pouring water on dark stones, steam rising, cedar walls", True),
            ("message", "What you want the post to say, if anything", "Thursday Aufguss is back", False),
        ],
        "body": (
            "Write for {{venue_name}}: (1) an Instagram caption of 20 to 60 words, (2) alt text of under 125 "
            "characters that plainly describes the photo.\n\nPhoto: {{photo_description}}\nMessage: {{message}}\n\n"
            "Alt text describes only what is visible, with no hashtags or marketing."
        ),
    },
    {
        "id": "newsletter",
        "category": "Social media",
        "title": "Monthly newsletter",
        "use_case": "A short email to members and past guests.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("news", "What is new, upcoming events, changes to hours or prices", "January Aufguss schedule; new cold plunge; price of 10-visit pass unchanged", True),
            ("cta", "The one thing you want readers to do", "Book a January session", True),
        ],
        "body": (
            "Write a newsletter for {{venue_name}} of 150 to 250 words, with a subject line under 50 characters and "
            "a preview line under 90 characters.\n\nNews:\n{{news}}\n\nMain call to action: {{cta}}\n\n"
            "One short section per news item, the call to action once near the end. Use only the news above."
        ),
    },
    {
        "id": "staff-answer-bank",
        "category": "Team",
        "title": "Answer bank for front-desk staff",
        "use_case": "Give new staff consistent answers to the questions guests ask most.",
        "variables": [
            ("venue_name", "Name of your venue", "Cedar & Steam Sauna Club", True),
            ("venue_facts", "Everything true staff may say: hours, prices, rules, facilities, policies", "(paste your facts sheet)", True),
            ("common_questions", "The questions guests ask, one per line", "How hot is it? Can I come alone? Do you sell hats?", True),
        ],
        "body": (
            "Write a front-desk answer bank for {{venue_name}}.\n\nFacts staff may use:\n{{venue_facts}}\n\n"
            "Questions:\n{{common_questions}}\n\n"
            "For each question: a one or two sentence answer staff can say aloud, based only on the facts. If the "
            "facts do not answer it, write [ASK OWNER]. For any question about health, the answer is: we cannot "
            "advise on that, please check with your doctor, and here is our house rule."
        ),
    },
]

VAR = re.compile(r"\{\{(\w+)\}\}")


def full_prompt(p):
    rules = [STYLE] + [g for _, g in CORE_GUARDRAILS] + p.get("extra_guardrails", [])
    return p["body"] + "\n\nRules:\n" + "\n".join("- " + r for r in rules)


def build():
    out = {
        "name": "Prompts for sauna and spa owners",
        "version": VERSION,
        "publisher": "DIVELUX (https://diveluxsaunahat.com)",
        "license": "CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)",
        "language": "en-US",
        "how_to_use": "Replace every {{variable}} with your own facts, then paste the prompt into any chat assistant. "
                      "Optionally set system_prompt first. Always read the result before sending it.",
        "system_prompt": SYSTEM_PROMPT,
        "core_guardrails": [{"id": i, "text": t} for i, t in CORE_GUARDRAILS],
        "prompts": [],
    }
    for p in PROMPTS:
        text = full_prompt(p)
        out["prompts"].append({
            "id": p["id"],
            "category": p["category"],
            "title": p["title"],
            "use_case": p["use_case"],
            "prompt": text,
            "variables": [{"name": n, "description": d, "example": e, "required": r} for n, d, e, r in p["variables"]],
            "guardrails": [i for i, _ in CORE_GUARDRAILS],
        })
    with open(os.path.join(HERE, "prompts.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")

    md = ["# Prompts for sauna and spa owners", "",
          "Version %s. %d prompts for replying to guests, writing house rules, planning Aufguss sessions and posting on social media. "
          "Made by [DIVELUX](https://diveluxsaunahat.com). License: CC BY 4.0." % (VERSION, len(PROMPTS)), "",
          "Replace every `{{variable}}` with your own facts, paste the prompt into any chat assistant, and read the answer "
          "before you send it. Every prompt carries the same rules, so it works when copied on its own.", "",
          "## Contents", ""]
    cats = []
    for p in PROMPTS:
        if p["category"] not in cats:
            cats.append(p["category"])
    for c in cats:
        md.append("- **%s:** %s" % (c, ", ".join("[%s](#%s)" % (p["title"], p["id"]) for p in PROMPTS if p["category"] == c)))
    md += ["", "## Optional system prompt", "", "Set this once as the assistant's instructions (custom instructions, a project, or a system message):", "",
           "```text", SYSTEM_PROMPT, "```", ""]
    for c in cats:
        md += ["## " + c, ""]
        for p in PROMPTS:
            if p["category"] != c:
                continue
            md += ['<a id="%s"></a>' % p["id"], "", "### " + p["title"], "", "*" + p["use_case"] + "*", "",
                   "| Variable | What to put in | Example |", "| --- | --- | --- |"]
            for n, d, e, r in p["variables"]:
                md.append("| `{{%s}}`%s | %s | %s |" % (n, "" if r else " (optional)", d, e.replace("|", "/")))
            md += ["", "```text", full_prompt(p), "```", ""]
    md += ["---", "", "Not medical advice. These prompts help you write; you are responsible for what you send. "
           "© 2026 DIVELUX Inc., CC BY 4.0. More free sauna tools: https://diveluxsaunahat.com/pages/sauna-tools", ""]
    with open(os.path.join(HERE, "prompts.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print("wrote prompts.json and prompts.md:", len(PROMPTS), "prompts")


if __name__ == "__main__":
    build()
