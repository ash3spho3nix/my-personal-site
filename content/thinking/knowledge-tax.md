---
title: "What AI Can't Inherit"
description: "On the difference between knowledge and experience, why AI systems can't replace an experienced engineer, and what a knowledge-graph-based RAG system can - and can't - do about it."
draft: false
---

While working on battery simulations at A123 during the day, and exploring AI systems on the side in the evenings, I kept running into the same wall: an AI system, no matter how many knowledge documents, simulation reports, or test results you feed it, cannot replace an experienced engineer. Not because it lacks knowledge - it can hold more documents than any one person ever will - but because what's missing isn't knowledge. It's experience.

Experience comes from working through problems, often with non-conventional methods that never made it into any document, because nobody thought to write them down, or because the method only makes sense in the context of the failure that produced it.

I think back to my time at TVS. There was a prototype mechanic there - much older than me, decades of hands-on experience - who could listen to an engine for a few seconds and tell you exactly where the problem was. Then he'd open it up with a spanner and fix it. At the time, I didn't really understand what I was watching. I do now. He wasn't running a diagnostic checklist in his head. He'd built, over years, an internal model of what a given sound meant - a mapping that no spec sheet or service manual contained, because it was never the kind of thing that gets written down.

That's the part that leaves when an engineer leaves, gets promoted, or just gets too busy to answer questions. Not the documents - those stay in the PLM, in Confluence, in shared drives. What leaves is the mapping between a symptom and a cause, built over years of being the person who got called when something didn't make sense.

So where does that leave AI systems in engineering orgs? Not as a replacement - that idea doesn't survive contact with reality. But maybe as a partial mitigation. A knowledge-graph-based RAG system - one that doesn't just store documents but tries to capture the relationships between a chemistry change, a process parameter, a test failure, and the fix that resolved it - could give a new engineer a head start. Not the mechanic's ear. But maybe a pointer toward the right question to ask, or the right old report or test log to go dig into.

That's the framing behind the [Battery Expert AI](/work/projects/battery-ai-systems/) work - it's deliberately not positioned as a replacement for engineering judgment. It's a retrieval layer that surfaces relevant prior work faster, so the engineer can get to the judgment part sooner. The [Codebase Indexer](/work/projects/codebase-indexer/) is the same idea applied to code: it doesn't understand *why* a module was built the way it was, but it can at least show you where to start looking.

The tribal knowledge tax is real, and I don't think it's solvable. But it might be reducible - and that's a more honest goal than the one most "AI will capture your institutional knowledge" pitches are selling.

---

## Connects To

*Thinking: [AI as Reasoning Infrastructure](/thinking/how-i-think/#ai-as-reasoning-infrastructure)*
*Project: [Battery Expert AI](/work/projects/battery-ai-systems/)*
*Project: [Codebase Indexer](/work/projects/codebase-indexer/)*
