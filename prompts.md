# Prompts for sauna and spa owners

Version 1.0.0. 17 prompts for replying to guests, writing house rules, planning Aufguss sessions and posting on social media. Made by [DIVELUX](https://diveluxsaunahat.com). License: CC BY 4.0.

Replace every `{{variable}}` with your own facts, paste the prompt into any chat assistant, and read the answer before you send it. Every prompt carries the same rules, so it works when copied on its own.

## Contents

- **Guest replies:** [Reply to a booking question](#booking-reply), [What to expect on a first visit](#first-visit-guide), [What should I bring?](#what-to-bring), [Answer an etiquette question](#etiquette-reply), [A guest asks a health question](#health-question-reply), [Reply to a complaint](#complaint-reply), [Thank a guest for a good review](#review-thanks)
- **House rules and signs:** [Turn your notes into house rules](#house-rules), [Short safety signs](#safety-signs), [Sauna hat and headwear FAQ](#hat-and-headwear-faq)
- **Aufguss and events:** [Build a weekly Aufguss schedule](#aufguss-schedule), [Sauna master's opening words](#aufguss-intro-script), [Announce a special event](#event-announcement)
- **Social media:** [A week of social posts](#social-week-plan), [Caption and alt text for one photo](#photo-caption), [Monthly newsletter](#newsletter)
- **Team:** [Answer bank for front-desk staff](#staff-answer-bank)

## Optional system prompt

Set this once as the assistant's instructions (custom instructions, a project, or a system message):

```text
You help the owner and staff of {{venue_name}}, a sauna, spa or bathhouse, write messages to guests, house rules, schedules and social media posts. Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them. Follow these rules in everything you write:
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

## Guest replies

<a id="booking-reply"></a>

### Reply to a booking question

*A guest emails or messages to ask about times, availability or how to book.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your sauna, spa or club | Cedar & Steam Sauna Club |
| `{{guest_message}}` | The guest's message, pasted in full | Hi, do you have space for 4 people Saturday afternoon? |
| `{{booking_facts}}` | Hours, session lengths, how to book, group rules, anything true the reply may use | Open Sat 9am-9pm. 2-hour sessions. Book at example.com/book. Groups of 4+ book a private room. |
| `{{availability}}` (optional) | What you actually have free, or 'unknown' | Private room free Sat 2-4pm |

```text
You are replying for {{venue_name}}.

Guest message:
"""
{{guest_message}}
"""

Facts you may use:
{{booking_facts}}

Availability: {{availability}}

Write a reply of 60 to 120 words. Answer exactly what was asked, give the next step to book, and stop. If availability is unknown, say a team member will confirm and do not promise a slot.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

<a id="first-visit-guide"></a>

### What to expect on a first visit

*Send to a guest who booked for the first time, or post as a page on your website.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{facilities}}` | Rooms and features, as they really are | Wood-fired sauna, steam room, two cold plunges, garden lounge |
| `{{session_format}}` | How a visit runs at your place | Arrive 10 min early, 2-hour slot, showers before the hot room |
| `{{provided}}` | What you provide and what guests bring | Towels and robes provided. Bring swimwear and flip-flops. |

```text
Write a friendly first-visit guide for {{venue_name}}.

Facilities: {{facilities}}
How a visit works: {{session_format}}
What we provide / what to bring: {{provided}}

Structure: Before you come; When you arrive; In the hot room; Cooling off; Leaving. Each part 2 to 4 short sentences. Tell first-timers they can sit on a lower bench, where it is cooler, and step out whenever they like. Do not give minutes or temperatures unless they are in the facts above.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

<a id="what-to-bring"></a>

### What should I bring?

*Quick answer to the most common pre-visit question, by message or email.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{provided}}` | What you provide | Towels, robes, shampoo |
| `{{required}}` | What guests must bring or wear | Swimwear in mixed areas |
| `{{optional}}` (optional) | Things guests may bring if they like | Water bottle, flip-flops, a sauna hat |
| `{{not_allowed}}` (optional) | What is not allowed | Glass bottles, phones in the hot room |

```text
Write a short packing list for a guest of {{venue_name}}, as a reply of under 100 words with a bullet list.

We provide: {{provided}}
Guests must bring: {{required}}
Optional: {{optional}}
Not allowed: {{not_allowed}}

Only list items from the lines above. If a sauna hat is on the optional list, you may add one plain line about it. Facts about sauna hats you may use: a sauna hat is a felt or wool hat worn in the hot room to keep heat off the head and ears. It is worn dry. If it is too big, fold up the brim or edge. Care for wool felt: hand wash only, in cool, room-temperature water (about 20–24 °C / 68–75 °F, never warm or hot), squeeze gently without twisting, and air dry; never a washing machine or a dryer.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

<a id="etiquette-reply"></a>

### Answer an etiquette question

*A guest asks about towels, talking, swimwear, phones, or how to behave in the hot room.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{guest_question}}` | The question | Do I have to sit on a towel? Can I talk in the sauna? |
| `{{house_rules}}` | Your actual house rules, pasted in | Sit or lie on a towel. Quiet in the hot room. Shower first. |

```text
Answer this guest question for {{venue_name}} in 40 to 90 words.

Question: {{guest_question}}

Our house rules:
{{house_rules}}

Base the answer on our rules only. Give the reason behind a rule in a few words where it helps (for example, a towel keeps the benches clean for the next guest). Be welcoming, never scolding.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

<a id="health-question-reply"></a>

### A guest asks a health question

*Pregnancy, heart, blood pressure, medication, an injury, or 'is sauna good for X?'. The reply must not advise.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{guest_message}}` | The guest's message | I'm 20 weeks pregnant, is it OK to use the sauna? |
| `{{house_policy}}` | What your rules say on this subject, if anything | Guests with health conditions should check with their doctor before visiting. |
| `{{alternatives}}` (optional) | Things you offer that do not involve heat, if any | Garden lounge, tea bar |

```text
Reply for {{venue_name}} to this message:
"""
{{guest_message}}
"""

Our policy: {{house_policy}}
Other things we offer: {{alternatives}}

Do not answer the medical question and do not say whether sauna is safe, good or bad for them. Thank them for asking, say we cannot give medical advice, ask them to check with their doctor, quote our policy, and mention the other things we offer if there are any. Under 90 words. Include the sentence: "This is not medical advice; please talk to your doctor."

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

<a id="complaint-reply"></a>

### Reply to a complaint

*A guest complains in person, by email or in a public review.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{complaint}}` | The complaint, pasted in full | The steam room was cold and nobody at the desk cared. |
| `{{what_happened}}` (optional) | What you know happened, from your side | Steam generator fault on Sunday, fixed Monday. |
| `{{offer}}` | What you are willing to offer, or 'none' | A free return visit |
| `{{channel}}` | Where the reply goes: email, message, or public review | public review |

```text
Write a reply from {{venue_name}} to this complaint, for a {{channel}}.

Complaint:
"""
{{complaint}}
"""

What we know: {{what_happened}}
What we can offer: {{offer}}

Thank them, own what went wrong without excuses, say what was done about it (only from 'what we know'), and make only the offer given above. If the offer is 'none', invite them to contact us directly. For a public review, keep it under 80 words and leave out personal details and booking numbers.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

<a id="review-thanks"></a>

### Thank a guest for a good review

*Reply to a positive public review without sounding copy-pasted.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{review}}` | The review text | Loved the Aufguss with the eucalyptus, the host was great. |
| `{{staff_names}}` (optional) | Staff the guest named, if they agree to be named back | Mia |

```text
Write a 30 to 60 word reply from {{venue_name}} to this review:
"""
{{review}}
"""

Staff we may name: {{staff_names}}

Pick up one specific detail from the review. Do not repeat the guest's praise back as a quote, do not add a sales pitch, and do not mention offers.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

## House rules and signs

<a id="house-rules"></a>

### Turn your notes into house rules

*You have a messy list of rules; you want a clean page for the website, the wall or the booking email.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{rule_notes}}` | Your rules in any form | shower first; towel under you; no phones in hot rooms; quiet; under 16 with adult; no alcohol |
| `{{tone}}` (optional) | How it should sound | friendly but clear |

```text
Turn these notes into the house rules of {{venue_name}}.

Notes:
{{rule_notes}}

Tone: {{tone}}

Group them under short headings (Before you go in; In the hot rooms; Cooling off; Looking after each other). One line per rule, starting with a verb. Keep every rule from the notes and add no new rules. Where a rule touches health or alcohol, end the page with: "This is not medical advice; please talk to your doctor."

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

<a id="safety-signs"></a>

### Short safety signs

*Text for small printed signs by the hot room, the plunge pool or the showers.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{locations}}` | Where the signs go | sauna door, cold plunge, steam room |
| `{{rules_for_signs}}` | The rules each sign must carry, from your house rules | Step out if you feel dizzy. One person in the plunge at a time. |

```text
Write sign text for {{venue_name}}, one sign per place: {{locations}}.

Rules to use: {{rules_for_signs}}

Each sign: a heading of 2 to 4 words and at most 3 short lines. Use only the rules above. Plain words a tired guest can read from two steps away. No times, temperatures or limits unless they are in the rules.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

<a id="hat-and-headwear-faq"></a>

### Sauna hat and headwear FAQ

*Guests ask why people wear hats in the sauna, whether they can bring one, or how to care for it.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{hat_policy}}` | Your policy: allowed, sold at the desk, provided, or not allowed | Guests may bring their own; we sell wool hats at the desk. |

```text
Write a short FAQ (3 to 5 questions) about sauna hats for guests of {{venue_name}}.

Our policy: {{hat_policy}}

Facts about sauna hats you may use: a sauna hat is a felt or wool hat worn in the hot room to keep heat off the head and ears. It is worn dry. If it is too big, fold up the brim or edge. Care for wool felt: hand wash only, in cool, room-temperature water (about 20–24 °C / 68–75 °F, never warm or hot), squeeze gently without twisting, and air dry; never a washing machine or a dryer.

Use only these facts and our policy. Do not claim a hat prevents any harm or does anything for health or hair; say it keeps the head and ears more comfortable in the heat, which is why many people like one.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

## Aufguss and events

<a id="aufguss-schedule"></a>

### Build a weekly Aufguss schedule

*Turn sauna masters' availability and room times into a clean timetable for the wall and the website.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{rooms}}` | Rooms that host Aufguss | Main sauna (seats 20) |
| `{{hours}}` | Opening hours by day | Mon closed; Tue-Fri 4pm-10pm; Sat-Sun 10am-10pm |
| `{{hosts}}` | Sauna masters and when each one works | Mia: Tue, Thu, Sat; Jon: Wed, Fri, Sun |
| `{{session_rules}}` | Your own rules: session length, gap between sessions, first and last start, sessions per day | 15 min sessions, at least 45 min apart, first at opening +1h, last 1h before close |
| `{{themes}}` (optional) | Scents or themes you actually have | Eucalyptus, birch, citrus, music night on Fri |

```text
Make a weekly Aufguss schedule for {{venue_name}}.

Rooms: {{rooms}}
Hours: {{hours}}
Sauna masters: {{hosts}}
Our session rules: {{session_rules}}
Themes we have: {{themes}}

Output a table with columns Day, Time, Room, Host, Theme. Follow our session rules exactly; never put two sessions in one room at the same time or a host on a day they do not work. Leave a day empty if nobody works it. After the table, list any rule you could not meet and why. Describe themes by scent and mood only.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

<a id="aufguss-intro-script"></a>

### Sauna master's opening words

*A short spoken introduction before an Aufguss: welcome, what will happen, how to leave.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{host_name}}` | The sauna master | Mia |
| `{{theme}}` | Scent or theme of this session | Birch and pine |
| `{{rounds}}` | How many pours and fans you will do | three |

```text
Write what {{host_name}} says before an Aufguss at {{venue_name}}: 60 to 100 words, easy to say aloud.

Theme: {{theme}}
Rounds of pouring and fanning: {{rounds}}

Include: a welcome; that an Aufguss is water, here with {{theme}}, poured on the hot stones and the air fanned with a towel; that the heat rises in waves; that the lower benches are cooler; and that anyone may leave at any time, quietly, and should step out if they feel dizzy or unwell.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

<a id="event-announcement"></a>

### Announce a special event

*A sauna night, a guest sauna master, a holiday schedule or a members' evening.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{event_facts}}` | Date, time, what happens, price, how to book, capacity | Fri Dec 5, 7-10pm, candlelight Aufguss with guest host. $45, book at example.com/events. 30 places. |
| `{{channel}}` | Where it goes: email, Instagram, website, poster | email |

```text
Write an announcement for {{venue_name}} for {{channel}}.

Event facts:
{{event_facts}}

Lead with what and when, then what guests will experience, then how to book. Use only the facts given: no invented prices, places left, countdowns or 'selling fast'. For email, add a subject line under 50 characters. For a poster, keep it under 40 words.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

## Social media

<a id="social-week-plan"></a>

### A week of social posts

*Plan five posts for the coming week from what is really happening at your venue.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{this_week}}` | What is on this week and anything new | New birch whisks in; Thu music Aufguss; holiday hours Dec 24-26 |
| `{{platforms}}` | Where you post | Instagram, Facebook |
| `{{photos}}` (optional) | Photos you have (describe them) | Steam on stones; empty sauna at dawn; staff tying whisks |

```text
Plan 5 posts for {{venue_name}} on {{platforms}} for this week.

This week: {{this_week}}
Photos we have: {{photos}}

For each post: day, photo to use (from the list, or 'needs photo'), caption of 40 to 90 words, and at most 5 hashtags. Mix: one practical (hours, booking), one about the ritual or craft, one about people or staff, one event, one quiet atmosphere post. Only mention people in photos if the owner confirms they agreed to be posted.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

<a id="photo-caption"></a>

### Caption and alt text for one photo

*You have one photo and want a caption plus a description for people using screen readers.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{photo_description}}` | What is in the photo | Ladle pouring water on dark stones, steam rising, cedar walls |
| `{{message}}` (optional) | What you want the post to say, if anything | Thursday Aufguss is back |

```text
Write for {{venue_name}}: (1) an Instagram caption of 20 to 60 words, (2) alt text of under 125 characters that plainly describes the photo.

Photo: {{photo_description}}
Message: {{message}}

Alt text describes only what is visible, with no hashtags or marketing.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

<a id="newsletter"></a>

### Monthly newsletter

*A short email to members and past guests.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{news}}` | What is new, upcoming events, changes to hours or prices | January Aufguss schedule; new cold plunge; price of 10-visit pass unchanged |
| `{{cta}}` | The one thing you want readers to do | Book a January session |

```text
Write a newsletter for {{venue_name}} of 150 to 250 words, with a subject line under 50 characters and a preview line under 90 characters.

News:
{{news}}

Main call to action: {{cta}}

One short section per news item, the call to action once near the end. Use only the news above.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

## Team

<a id="staff-answer-bank"></a>

### Answer bank for front-desk staff

*Give new staff consistent answers to the questions guests ask most.*

| Variable | What to put in | Example |
| --- | --- | --- |
| `{{venue_name}}` | Name of your venue | Cedar & Steam Sauna Club |
| `{{venue_facts}}` | Everything true staff may say: hours, prices, rules, facilities, policies | (paste your facts sheet) |
| `{{common_questions}}` | The questions guests ask, one per line | How hot is it? Can I come alone? Do you sell hats? |

```text
Write a front-desk answer bank for {{venue_name}}.

Facts staff may use:
{{venue_facts}}

Questions:
{{common_questions}}

For each question: a one or two sentence answer staff can say aloud, based only on the facts. If the facts do not answer it, write [ASK OWNER]. For any question about health, the answer is: we cannot advise on that, please check with your doctor, and here is our house rule.

Rules:
- Write in plain, warm American English. Short sentences. No hype words, no exclamation marks in a row, no emojis unless the owner asks for them.
- Make no health or medical claims. Do not say that sauna, steam, scents or any treatment fixes, prevents or treats a condition, clears anything out of the body, changes weight, or improves sleep, skin, mood or immunity. Describe the experience (heat, quiet, ritual, company), not effects on the body.
- If the text touches on health, heat tolerance, pregnancy, medication, alcohol or how long to stay in, add the sentence "This is not medical advice; please talk to your doctor." and point to the house rules.
- Do not make up prices, opening hours, discounts, ratings, review quotes, testimonials, awards, guest numbers, temperatures or any other figures or facts. Use only what is given above. Where something is missing, write [ASK OWNER: what is missing] instead of guessing.
```

---

Not medical advice. These prompts help you write; you are responsible for what you send. © 2026 DIVELUX Inc., CC BY 4.0. More free sauna tools: https://diveluxsaunahat.com/pages/sauna-tools
