# Prompts for sauna and spa owners

17 copy-and-paste prompts for the people who run saunas, spas, bathhouses and sauna clubs: replies to guests, house rules and signs, Aufguss schedules and event announcements, social posts and a front-desk answer bank. They work with any chat assistant.

Made by [DIVELUX](https://diveluxsaunahat.com), a small family brand in Irvine, California that makes handmade wool sauna hats.

Every prompt carries the same three rules, so it stays safe when you copy just one:

1. **No health claims.** Describe the experience (heat, quiet, ritual, company), never effects on the body.
2. **"Not medical advice."** Anything that touches health, pregnancy, medication, alcohol or how long to stay in gets the line *This is not medical advice; please talk to your doctor* and a pointer to your house rules.
3. **No invented facts.** No made-up prices, hours, discounts, ratings, review quotes, awards or temperatures. Where a fact is missing, the assistant writes `[ASK OWNER: ...]` instead of guessing.

## The prompts

| Group | id | Prompt |
| --- | --- | --- |
| Guest replies | `booking-reply` | Reply to a booking question |
| Guest replies | `first-visit-guide` | What to expect on a first visit |
| Guest replies | `what-to-bring` | What should I bring? |
| Guest replies | `etiquette-reply` | Answer an etiquette question |
| Guest replies | `health-question-reply` | A guest asks a health question (the reply does not advise) |
| Guest replies | `complaint-reply` | Reply to a complaint |
| Guest replies | `review-thanks` | Thank a guest for a good review |
| House rules and signs | `house-rules` | Turn your notes into house rules |
| House rules and signs | `safety-signs` | Short safety signs |
| House rules and signs | `hat-and-headwear-faq` | Sauna hat and headwear FAQ |
| Aufguss and events | `aufguss-schedule` | Build a weekly Aufguss schedule |
| Aufguss and events | `aufguss-intro-script` | Sauna master's opening words |
| Aufguss and events | `event-announcement` | Announce a special event |
| Social media | `social-week-plan` | A week of social posts |
| Social media | `photo-caption` | Caption and alt text for one photo |
| Social media | `newsletter` | Monthly newsletter |
| Team | `staff-answer-bank` | Answer bank for front-desk staff |

Read them in [`prompts.md`](prompts.md), or load [`prompts.json`](prompts.json) into your own tool.

## How to use one

1. Open `prompts.md` and find the prompt.
2. Copy the text block. Replace each `{{variable}}` with your own facts; the table above each prompt says what goes where and shows an example.
3. Paste it into your assistant. If your assistant has custom instructions or a system message, you can set the **system prompt** at the top of `prompts.md` once.
4. Read the answer before you send or post it. You know your venue; the assistant does not.

The prompts ask only for facts you give them. The more of your real hours, prices and rules you paste in, the less the assistant has to leave as `[ASK OWNER]`.

## JSON format

```json
{
  "name": "Prompts for sauna and spa owners",
  "version": "1.0.0",
  "system_prompt": "You help the owner and staff of {{venue_name}} ...",
  "core_guardrails": [{ "id": "no-health-claims", "text": "..." }, ...],
  "prompts": [
    {
      "id": "booking-reply",
      "category": "Guest replies",
      "title": "Reply to a booking question",
      "use_case": "A guest emails or messages to ask about times ...",
      "prompt": "You are replying for {{venue_name}}. ... Rules: ...",
      "variables": [{ "name": "venue_name", "description": "...", "example": "...", "required": true }],
      "guardrails": ["no-health-claims", "not-medical-advice", "no-invented-facts"]
    }
  ]
}
```

`prompt` is complete: it already ends with its Rules block. Fill it with a plain string replace of `{{name}}`.

## About the sauna hat FAQ

`hat-and-headwear-faq` and `what-to-bring` give the assistant a short, fixed set of facts: a sauna hat is a felt or wool hat worn in the hot room to keep heat off the head and ears; it is worn dry; if it is too big, fold up the edge; wool felt is hand washed only, in cool, room-temperature water (about 20–24 °C / 68–75 °F, never warm or hot), squeezed gently without twisting and air dried, never machine washed or tumble dried. The prompt forbids health or hair claims for hats.

## Checks

```sh
python3 build.py      # regenerates prompts.json and prompts.md from the definitions in build.py
python3 validate.py
```

`validate.py` (standard library only) checks the JSON shape, unique ids, that every `{{variable}}` is declared and every declared one is used, that each prompt carries the three core rules word for word, that `prompts.md` matches the JSON, and scans both files for banned wording: *detox, toxins, cure, heal, burn fat, weight loss, boost immunity, anti-aging, clinically, scientifically proven, miracle, guarantee, #1, five-star*, and anything about getting a sauna hat *wet, soaked, damp* or *wrung*. Last run:

```text
17 prompts, 5 categories, 62 variables
OK
```

The prompts were written and checked by hand. They were not benchmarked against particular assistants; outputs vary between tools and versions, which is why step 4 above matters.

## License

Prompt texts (`prompts.md`, `prompts.json`): [CC BY 4.0](LICENSE), © 2026 DIVELUX Inc. Use them in your business, change them, share them; credit "DIVELUX, diveluxsaunahat.com" when you republish the collection. The texts you generate with them are yours. Scripts (`build.py`, `validate.py`): [MIT](LICENSE-CODE).

Not medical advice. These prompts help you write; you are responsible for what you send.

More free sauna tools: <https://diveluxsaunahat.com/pages/sauna-tools>
