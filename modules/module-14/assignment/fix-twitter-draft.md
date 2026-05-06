# Module 14 Individual Assignment — Fix Twitter

**Course:** SWE 632 — User Interface Design<br>
**Author:** Laws Smith<br>
**Due:** April 27, 2026

I don't use Twitter / X much, so my read on it is mostly what I hear from others and what leaks out into news. Two problems jump out though, and they map pretty cleanly to community design ideas from this module.

## Problem 1: People are mean to each other on it

One concern I've heard about Twitter / X (or really most similar online platforms) is how hostile it can be. When everyone is a stranger, it is easy to accuse and belittle without considering discourse or humanity. Instead of listening and taking someone's opinion into consideration, it is easier to just listen to oneself and mark others as wrong or eveil. A lot of this comes back to one thing. The platform is built to let you talk *at* anyone, but it does almost nothing to make you feel like you're talking *to* a person.

The module framed this in terms of bonds-based commitment, the idea that what makes a community pull people back, and what makes them care about how they behave in it, is feeling close to specific other members. Twitter has the opposite design. The default experience is interacting with strangers via the algorithm. There's no friction between you and someone you've never spoken to, and there's no signal in the UI for how socially close you actually are to the person you're replying to.

A few changes I'd make:

- Show social distance on every interaction: When I'm about to reply to someone, the compose box should tell me whether we have any mutuals, any shared communities, or zero overlap. Same for replies I receive. That information is already in the social graph, surface it. The "stranger yelling at strangers" dynamic gets harder when the UI quietly reminds you these are real people you have, or could have, real connections to.
- Default new accounts to a smaller circle: Drop the firehose. New accounts should land in a mutuals-and-mutuals-of-mutuals feed first, and have to opt into the global feed. A lot of what's poisonous about Twitter is a network-scale problem. Constraining the default scale to people you'd actually meet in real life starts to fix it.
- Make norms salient the way a workplace-injury sign does: The lecture's "X days since last incident" example fits here. Instead of only seeing the worst replies on a post (which the algorithm already amplifies because they generate engagement), show me the good ones too. Replies from people who corrected something kindly, asked a real question, or changed their mind. Publicly contrasting normative behavior with the bad stuff is one of the cheapest tools we have, and Twitter does almost none of it.
- Cut the dunk loop: Quote-tweets used as a way to drag a stranger in front of your followers are basically the dislike button Facebook decided not to ship, except worse, because they come with a megaphone attached. I'd add friction to quote-tweets across a big follower-count gap, default them to a non-mocking response template, or fall back to a regular reply. Not censoring, just removing the one-tap dunk.

## Problem 2: It's getting impossible to tell what's real

The other thing I'd want to address is that I can't tell, looking at any given post, whether it's a person, a bot, a paid account, or AI-generated content. I can't tell whether a claim is somebody's opinion, somebody quoting a study, or somebody confidently making something up. The current "blue check" answers none of those questions, it just says someone paid eight dollars.

I don't want to restrict what people can say. I do want the platform to do a better job of telling me what kind of thing I'm reading. The module's fourth design dimension is roles, rules, access control, and visibility. Communities can hand out specialized roles, badges, and visibility differently for different kinds of content. Twitter lumps everything into one shape on purpose, and that's the design choice that makes the misinformation problem so bad.

A few changes:

- Replace the paid checkmark with a stack of small, earned indicators: Instead of one blue badge meaning "paid," I'd have a small set. Identity verified (matches a government ID), credential verified (this account is run by a journalist at a real outlet, or a published researcher in a stated field), organizational verified (the account belongs to the org it claims to). Each one is narrow, each one is earned, and each one is removable. None of them confer extra reach the way the current blue check does.
- Self-tag posts as opinion, claim, or report: When you post, you pick one. Opinion is the default. Claim means you're stating something as factual, and if you tag it as a claim the post gets a slot for a source link and the UI prompts you for one. Report means you're describing something you witnessed yourself. You don't have to use the right tag, but if a Community-Notes-style review shows your claim posts are repeatedly unsourced or wrong, you lose claim privileges for a while. That pulls from the module's idea of access control as a regulator. Gating the action, not the speech.
- AI-content labels, surfaced not buried: Any post or media generated with AI gets a clear label. Self-disclosure is one path, but the bigger lift is platform-side metadata detection (C2PA-style provenance for images, model-watermark detection for text where it works). The label belongs on the post itself, not three menus deep. The lecture listed "expressing truth to users and hiding misinformation" as a designer value. This is what that looks like in practice.
- Distinct visual treatment for opinion vs. sourced: Once a post is tagged as a claim and has a source linked, it should look different than a hot take. Different border, different background, something. Right now everything renders identically and that flattening is part of the problem.

## Closing

Both of these problems are really the same problem at different layers. The platform is designed for cheap, frictionless, low-context interaction, and a lot of the harm comes from that frictionlessness scaling badly. The fixes aren't about telling people what to say. They're about giving the interface enough texture (social distance, role badges, content tags, visible norms) that users have a reason to behave like they're in a room with other people, and a way to tell what kind of thing they're reading.
