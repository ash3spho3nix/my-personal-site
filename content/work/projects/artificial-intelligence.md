# The Black Box That Bothered Me Enough to Open It

## A Mechanical Engineer Walks Into a Neural Network

I need to be honest about something.

When ChatGPT exploded into public consciousness, I felt left behind. Everyone was talking about it. Using it. Marvelling at it. And I was sitting there thinking: I have no idea what is actually happening inside that thing.

That bothered me more than it should have.

You see, I have never liked black boxes. In my simulation work, I need to know why a model behaves a certain way. Is it a physics limitation? A numerical instability? A mistake in my boundary conditions? If I cannot explain the failure, I cannot fix it.

So I started digging. Slowly. Relentlessly. The same way I once dug into [contact mechanics](https://en.wikipedia.org/wiki/Contact_mechanics) and [optimization](https://en.wikipedia.org/wiki/Mathematical_optimization).

What I found surprised me. The massive language models everyone was obsessing over? They are built on concepts I already knew. Just scaled up. Way up.

---

## The Humble Beginning That No One Talks About

Back in 2013, I was playing with [neural networks](https://en.wikipedia.org/wiki/Neural_network). It was not the talk of the town back then. Deep learning was still finding its footing. Most engineers I knew were skeptical.

I did not care about the hype. I just found the idea fascinating.

A neural network is simple at its core. A bunch of numbers connected together in layers. You feed in inputs. They get multiplied by weights and transformed through activation functions. Out comes a prediction. Then you compare that prediction to the truth and adjust the weights slightly. Repeat a million times.

That is it. That is the engine.

I built small ones. Toy problems. Recognizing handwritten digits. Approximating simple functions. Nothing impressive by today's standards. But I understood those networks. I could look at the weights and tell you what each neuron was doing.

Fast forward a decade. Those same simple networks, stacked hundreds of layers deep and trained on the entire internet, became the foundation of [Large Language Models](https://en.wikipedia.org/wiki/Large_language_model). Same math. Same principles. Just a different scale that feels like magic but is not.

---

## The One Concept That Changed Everything

For years, neural networks struggled with sequences. Sentences. Time series. Anything where order mattered.

You would feed a network a sentence word by word. By the time it reached the end, it had forgotten the beginning. Recurrent networks helped a bit but were still fragile.

Then came [Attention Mechanisms](https://en.wikipedia.org/wiki/Attention_(machine_learning)). And honestly, the simplicity of it still amazes me.

Here is the idea. Instead of processing words in order, the network looks at all words simultaneously. For each word, it asks: which other words are relevant to understanding this one? It calculates attention scores. A little bit of attention goes to nearby words. Sometimes a lot of attention goes to a word from much earlier in the sentence.

"It" pays attention to the noun from five words ago. "He" pays attention to the name from the previous sentence.

That is it. That is the breakthrough. One simple mechanism that lets models handle long-range dependencies without breaking a sweat.

I remember reading the [Transformer paper](https://arxiv.org/abs/1706.03762) and laughing. Not because it was funny. Because it was obvious in retrospect. Of course that is how you do it. Pay attention to what matters. Ignore what does not.

The [Transformer architecture](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) built everything around this attention idea. No recurrence. No sequence processing. Just attention, feed-forward layers, and normalization. Stacked dozens of times.

This became the architecture behind every major LLM today.

---

## How Words Become Numbers

One piece of the puzzle confused me for a long time.

Neural networks do not understand words. They understand numbers. So how do you feed English sentences into a mathematical function?

The answer is [Embeddings](https://en.wikipedia.org/wiki/Word_embedding).

You map each word to a point in a high-dimensional space. Not a simple one-to-one mapping like a dictionary. Each word becomes a vector of maybe 300 or 768 or 4096 numbers. The magic is in how these vectors are arranged.

Words with similar meanings end up close together in this space. "King" and "Queen" are near each other. "Running" and "Walking" are in the same neighborhood. But it gets weirder. The directions in this space encode relationships. "King" minus "Man" plus "Woman" gets you close to "Queen". The vector arithmetic actually works.

This [vector space](https://en.wikipedia.org/wiki/Vector_space) of meanings is not programmed by hand. The network learns it from data. Millions of sentences. Billions of words. The geometry of language emerges from pure statistics.

I spent weeks just thinking about this. Words as points in space. Meaning as geometric relationships. It felt like discovering a secret law of language that no one had written down before.

---

## From Shy User to Architect

Let me tell you how my relationship with these models changed.

At first, I was a shy user. I would type a prompt nervously. If the model gave a bad response, I blamed the model. "Stupid AI." "Another hallucination." "This thing is broken."

That was unfair. And wrong.

Once I understood what was happening under the hood, I stopped blaming the model. I started blaming my own laziness.

The model is not thinking. It is doing pattern matching in a high-dimensional vector space. It does not know what it does not know. It has no internal compass for truth. It just predicts the next most probable token based on everything it has seen.

So when it fails, the failure is almost always predictable.

Give it a task outside its training distribution? It will fail. Give it ambiguous instructions? It will guess wrong. Give it no [context](https://en.wikipedia.org/wiki/Context_(computing)) about the problem? It will hallucinate confidently.

I learned to stop being a passive user. I became a prompt engineer without calling it that. I learned to set up [context engineering](https://en.wikipedia.org/wiki/Prompt_engineering) – providing the right background information before asking the question. I learned to break tasks into steps. To ask the model to show its reasoning. To give it examples of what a good answer looks like.

More recently, I discovered [Model Context Protocol](https://modelcontextprotocol.io) or MCP. This is a game changer. Instead of copying code into a prompt, the model can query tools directly. It can search your codebase. Run analyses. Fetch documentation. The model stops being a text generator and becomes an agent that can act.

I am still learning terms like [skill development](https://en.wikipedia.org/wiki/Competence_(human_resources)) for agents and harness engineering. But the direction is clear. These systems are tools. Powerful ones. But tools nonetheless.

Knowing where they fail is as important as knowing where they succeed.

---

## The Perspective No One Talks About

Here is what I wish someone had told me earlier.

A large language model is not a brain. It is a map of human language. A map that captures patterns, correlations, and statistical regularities. Nothing more. Nothing less.

That map is incredibly useful. You can navigate it to generate text. Summarize documents. Write code. Translate languages. But the map is not the territory. The model has never seen the real world. It has only seen descriptions of the world.

This explains every limitation you have heard about. Hallucinations happen because the model has no truth anchor. Bias happens because the training data contains bias. Reasoning failures happen because the model is doing pattern completion, not logical deduction.

I come from mechanics and simulation. In my world, a model is only as good as its governing equations and boundary conditions. You validate it. You test its limits. You know where it breaks.

Same thing applies here.

I do not blame ChatGPT for being wrong anymore. I blame myself for not giving it the right context. I do not get frustrated when it misunderstands. I refine my prompt. I add constraints. I give examples.

This shift – from user to architect – took me a while. But it was worth it.

---

## Where I Am Now

I still prefer Newton's laws to neural networks on most days. Give me a differential equation and a boundary condition. I will solve it happily.

But I no longer dismiss LLMs as black-box magic. I see them for what they are. Attention mechanisms stacked on embeddings stacked on neural networks. All powered by the same linear algebra I learned years ago. Just scaled to dimensions I cannot visualize and trained on data I cannot comprehend.

I still dig into failures. I still ask why. That splinter in my mind never went away.

But now, when an LLM gives me a strange answer, I do not shrug. I open the box. I look at the context I provided. I check the prompt structure. I think about the embedding space and what the model is actually retrieving.

Most of the time, the fault is mine. And that is good news. Because my faults I can fix.

---

*Links used in this article:*

- [Contact mechanics](https://en.wikipedia.org/wiki/Contact_mechanics)
- [Mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Neural network](https://en.wikipedia.org/wiki/Neural_network)
- [Large language model](https://en.wikipedia.org/wiki/Large_language_model)
- [Attention mechanism](https://en.wikipedia.org/wiki/Attention_(machine_learning))
- [Transformer (machine learning model)](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))
- [Word embedding](https://en.wikipedia.org/wiki/Word_embedding)
- [Vector space](https://en.wikipedia.org/wiki/Vector_space)
- [Context (computing)](https://en.wikipedia.org/wiki/Context_(computing))
- [Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)
- [Competence (human resources)](https://en.wikipedia.org/wiki/Competence_(human_resources))