---
title: "Exploring Local LLMs"
description: "How running local AI on a 4 GB GPU taught me more about LLMs than any course, tutorial, or benchmark ever could."
draft: false
---

![](/images/local-llm-workflow.png)

Around mid-2024, I was already using ChatGPT, Claude and various coding assistants almost daily. They were useful, sometimes surprisingly useful, but I was never completely comfortable with them. Everything felt like a black box. You type a question into a chat window, something magical happens behind the scenes, and an answer appears. Sometimes brilliant, sometimes completely wrong, but nobody really explains what happened in between.

As an engineer, that bothered me. I can accept complexity. I struggle with magic.

At the time I was reading more and more discussions around local LLMs. Ollama was becoming popular. LM Studio was everywhere on YouTube. People were running Llama models on laptops and talking about quantisation, context windows and embeddings as if these were everyday concepts. The idea itself was exciting. Not because I wanted to replace ChatGPT, and not because I had strong opinions about privacy. I simply wanted to know if I could run one myself.

*The same way I learned simulation software years ago. Install it. Break it. Fix it. Repeat.*

## My First Local Model

It started with installation of Ollama and LM Studio, downloaded Llama-3 Q4. Opened a terminal, followed a tutorial. That was the entire plan.

I had no idea what quantisation meant. I had never heard of KV cache. Context windows sounded vaguely familiar but I certainly didn't understand their implications. The model started successfully and I asked what was probably the most boring first question possible:

```bash
ollama run llama3

>>> What can you do?
````

The response appeared. That was the moment.

Not because the answer was impressive. ChatGPT could have produced a better answer. Claude could have produced a better answer. What felt different was the fact that the answer came from my own machine.

*No cloud. No API. No subscription. No company server somewhere across the world.*

**My machine generated that response.**

That small moment was enough to pull me down the rabbit hole.

## When Things Started Breaking

By this time I had already started experimenting with coding assistants. Continue, Roo Code, Cline, Aider, Kilo Code, OpenRouter integrations - I was trying almost everything I could find. My goal was simple; to know what is this exactly. I didn't want to become the AI engineer, nor I want to build another ChatGPT. I want to use this tool like a power user and borderline developer and not as a naive user.

I wanted my personal local coding assistant. I had so many ideas which suddenly began to seems implementable. Small utility ideas to big project ideas. From LLM taunting me about my git commit history to LLM finding me the forgotten pdf i saved 2 years back, from writing a self-driving RL car program to make an overnight running RAG and knowledge base system. 

*Unfortunately, reality had other plans.*

The models forgot instructions. They lost context. They hallucinated APIs. Sometimes they confidently generated nonsense while sounding extremely convincing. Tutorials kept mentioning concepts such as context windows, hallucinations, memory and attention mechanisms, but the explanations rarely answered the question I actually had.

### Why is this happening?

More importantly:
* What exactly is the model doing internally when it fails?
That question changed my learning path completely.

I learnt prompting techniques, but still failed, that's when I started learning how LLMs actually worked.

## Concepts That Finally Started Making Sense

The first useful concept was **tokens**.

A token is the basic currency of an LLM. Not words, not sentences — tokens. Every prediction, every generated response, every piece of context eventually becomes a sequence of tokens.

Once I understood tokens, context windows suddenly made sense.

A **context window** is simply the amount of information the model can actively keep inside its working memory during inference. Exceed that limit and the model starts forgetting earlier information, much like trying to remember an entire book while reading page 500.

Then came **attention mechanisms**.

Attention answers a simple question: out of thousands of previous tokens, which ones are important right now? This single idea explained why models could reason across large pieces of text and why they sometimes focused on the wrong information.

Then came **KV Cache**.

This was one of those concepts that suddenly explained every GPU memory problem I had been seeing. KV Cache stores intermediate attention information so the model doesn't need to recalculate everything repeatedly. Faster inference, but increased memory consumption.

Suddenly my GPU overflows started making sense. 

** This is where I started tweaking the model parameters, p-value, temperature, context window, penalty function, etc. The cycle of tweaking and watching the outputs, over and over, until I found that perfect setting for my local model**

Finally came **quantisation**.

Reducing model precision from FP16 to formats such as Q4_K_M was effectively the difference between "cannot run" and "runs successfully". Quantisation taught me that engineering is often about preserving enough information rather than preserving all information.

The black box was slowly becoming transparent.

I also grew my arsenal from Llama-3 to now deepseek-r1, qwen2.5-coder, codellama.

## The 900-Page Problem

Around the same period I faced a practical problem at work.

There was an internal document of roughly 900 pages. It appeared in almost every second meeting. Every discussion referenced it. Every investigation required searching through it. 

Uploading it to ChatGPT was not an option. Uploading it to Copilot was not an option. So a different question appeared.

*What if the document never leaves my machine? What if I bring the AI to the document instead?*

That question eventually became my first serious RAG system.

The first version was terrible. Retrieval quality was weak. Chunking strategies were wrong. Latency was high. The model frequently ignored the most relevant information. Version two improved retrieval. Version three improved ranking. Slowly it became useful.

More importantly, I started understanding why RAG systems fail. That understanding eventually influenced projects like Learning Journal, Battery Expert AI and later Alchemist.

## Why I Stayed With a 4 GB GPU

People occasionally ask why I kept using a 4 GB GPU instead of simply buying more hardware.

The answer is simple : **Scarcity is an excellent teacher.**

When resources are abundant, poor architecture often survives unnoticed. When resources are scarce, every design mistake becomes visible, every poor architectural implementation becomes the pain-point.

A 4 GB GPU forced me to understand:

* VRAM management
* Quantisation trade-offs
* Context optimisation
* Retrieval quality
* Inference bottlenecks
* Model selection

Every megabyte mattered. Every token mattered. Every design decision mattered. The hardware refused to hide my mistakes.

## The Shift Toward Hybrid Systems

The biggest lesson was not about models. It was about responsibility.

Initially I expected the LLM to solve everything. Most people still approach AI systems this way. Give the model a large prompt, hope for the best, then blame the model when something goes wrong.

Over time I realised many problems should never reach the LLM at all. Search should be handled by search. Static analysis should be handled by static analysis. Dependency graphs should be generated by code. Rules should be implemented using rules. The LLM should only solve problems that genuinely require reasoning or generation.

That realisation directly influenced projects like Codebase Indexer and Hybrid Code Analyzer.

```text
Code Repository
       │
       ▼
Codebase Indexer
(Symbol Graphs,
Dependencies,
Importance Scores)
       │
       ▼
Hybrid Code Analyzer
(Static + Dynamic Analysis)
       │
       ▼
MCP Interface
       │
       ▼
Local LLM
       │
       ▼
Reasoned Response
```

A typical MCP configuration looked something like:

```json
{
  "mcpServers": {
    "indexer": {
      "command": "python",
      "args": ["-y","indexer_bridge_server.py"]
    },
    "analyzer": {
      "command": "python",
      "args": ["-y", "analyzer_bridge_server.py"]
    }
  }
}
```

The LLM was no longer the entire system. It became one component inside a larger architecture. Not a tool, not a project but a part of an ecosystem.

## Looking Back

Today I still use ChatGPT, Claude and other proprietary models. They are incredibly capable and often outperform local models by a significant margin. That was never the point.

Running local LLMs changed how I think about intelligence itself.

I no longer see a chat window. I see tokens flowing through an attention network. I see context management, retrieval systems, memory constraints, embeddings and probability distributions working together to predict the next token. The magic disappeared, but something more valuable replaced it.

Understanding.

The local models were slower. They were smaller. They made more mistakes. Yet they taught me more about AI than any benchmark, tutorial or YouTube video ever could. I tried courses but that was all theory, my quest was for something more hands-on, something raw. The constraints forced me to learn the machinery underneath. I saw my machine literally running at its peak potential, GPU at 100% usage, GPU temperature rising. I saw how models broke, how one line in system prompt, one tweak in parameters, one change in prompt, can fix the problem of wrong outputs.

I use all propriertary models now, but this 'working' local llm setup is my personal achievement.

And once the machinery became visible, the real engineering started. 

