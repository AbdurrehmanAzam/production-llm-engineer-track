| **AI ENGINEERING ROADMAP**  **★ 1000 / 1000 — ULTIMATE EDITION — 2026 ★**  **TRACK A — LLM APPLICATION ENGINEER**  MCP · Hybrid RAG · Eval-First CI/CD · LangGraph · LiteLLM · vLLM · Langfuse |
| --- |

| *From Zero to Production-Grade LLM Engineer in 2026* |
| --- |

| **14+**  Total Phases | **220+**  Free Resources | **~571 hrs**  Total Hours | **12–15 mo**  Student Pace | **1000/1000**  Quality Score |
| --- | --- | --- | --- | --- |

## **👤 Student Profile**

| **Name** | Muhammad Abdurrehman Azam |
| --- | --- |
| **University** | USTB — University of Science and Technology Beijing |
| **Track** | LLM Application Engineer (Track A) — RAG · Agents · LLM APIs · Evals · FastAPI · LiteLLM · MCP |
| **Goal** | First job as AI / LLM Engineer within 12–15 months, then FAU Erlangen-Nürnberg MSc in AI |
| **Languages** | Native Urdu/Hindi, fluent English. Uses CampusX (Hindi/Urdu) for DSA/ML reinforcement |
| **Hardware** | RTX 4060 (8 GB VRAM) — enables unsloth + QLoRA fine-tuning locally with no API cost |
| **Tools** | Python 3.12 · uv · VS Code + Continue.dev + Cursor · WSL2 · Git · GitHub |
| **Status (2026-05-29)** | Phase 1 complete · Phase 2 in progress (3 problems solved) · Phase 3 & 3B complete |

## **★ What's New in 2026**

|  | **★ 2026 NEW**  Phase 3C — Prompt Engineering Patterns | Phase 5B — Document Parsing & Chunking | Security & Guardrails (Phase 7) | Memory Architecture (Phase 9) | Context Window Management | Embedding Evaluation | Interview Prep | Portfolio Phase |
| --- | --- |

|  | **⚠ NOTE**  Net addition: +43h (trimmed from +71h). Updated total: ~571h. Fits 12–15 month student pace at 10–15 hrs/week. |
| --- | --- |

## **🏷️ Badge Legend**

| **Badge** | **Action Required** | **Meaning — Exactly What to Do** |
| --- | --- | --- |
| **▶ WATCH ALL** | Watch entire video | Watch every single minute — nothing skippable. If it says WATCH ALL, 1× speed is fine. |
| **◈ SELECTIVE** | Read specified parts | Watch or read only the parts specified in the Notes column. Skipping unlisted parts is correct. |
| **⚙ PRACTICE** | Code in your editor | Hands-on only. Open your editor, write real code, commit to GitHub. No passive watching. |
| **◉ READ** | Read specified parts | Read thoroughly. Keep the tab open while coding. This is the primary definitive reference. |
| **◎ READ** | Read specified parts | Lighter reference. Consult when the primary source is unclear. Skim headings first. |

|  | **💡 TIP**  ☐ checkbox before every resource = progress tracker. Print or use in Word and tick each resource as you complete it. Every link is Ctrl+Clickable in Word. |
| --- | --- |

## **📋 Table of Contents**

| **Phase** | **Title** | **Timeline** | **Hours** |
| --- | --- | --- | --- |
| **Phase 1** | Advanced Async Foundations & Structured Data | 5 weeks | **~60h** |
| **Phase 2** | Algorithmic Literacy — Daily NeetCode Routine | Continuous | **30 min/day** |
| **Phase 3** | Dev Environment, Tooling & Model Context Protocol | 1 week | **~15h** |
| **Phase 3C ★** | Prompt Engineering Patterns (NEW 2026) | 1 week | **~10h** |
| **Phase 4** | Mathematical Intuition & Foundations | 2 weeks | **~20h** |
| **Phase 5** | Structured Engineering & Registry Pipelines | 2 weeks | **~25h** |
| **Phase 5B ★** | Document Parsing & Chunking Strategies (NEW 2026) | 1 week | **~15h** |
| **Phase 6** | Vector Processing, Redis Caching & Hybrid Retrieval | 3 weeks | **~51h** |
| **Phase 7** | Production API · Eval CI/CD · Security · Context Mgmt | 5 weeks | **~89h** |
| **Phase 8** | Deep Learning Internals & Open-Source Serving | 3 weeks | **~45h** |
| **Phase 9** | Stateful Multi-Agent Graph Engineering & Memory | 4 weeks | **~68h** |
| **Phase 10** | Production Capstone — Enterprise Answer Engine | 4 weeks | **~60h** |
| **Phase 11** | Interview Prep — LLM System Design | 2 wks (parallel) | **~10h** |
| **Phase 12** | Portfolio Website — Final Packaging | 1 weekend | **~8h** |

| **TOTAL HOURS ~571h (Core phases only)** | **TIMELINE 12–15 months @ 10–15 hrs/week** |
| --- | --- |

| **PHASE 1** │ **Advanced Async Foundations & Structured Data** |
| --- |
| ⏱ 5 weeks (~60 hours) │ ⚙ Core Stack: Python 3.12 · uv · Pydantic V2 · AsyncIO · Git |

Every later phase depends on this one. AsyncIO is not optional — every production LLM endpoint streams tokens asynchronously. Pydantic V2 is not optional — LLMs return unstructured JSON that must be validated at the boundary. Complete this phase before touching any LLM API.

|  | **✔ DELIVERABLE**  Phase 1 Lab: Run uv init. Write a script that (1) concurrently fetches JSON from 3 mock APIs using asyncio.gather(), (2) validates output with Pydantic V2 BaseModel + field validators, (3) writes results asynchronously to a file, (4) prints timestamps proving parallelism. Commit to GitHub with a green Actions badge. |
| --- | --- |

### **1.1 Python Core (3 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Bro Code — Python Full Course (12 hrs)](https://www.youtube.com/watch?v=XKHEtdqhLK8) | **YouTube** | **◈ SELECTIVE** | Chapters 1–9 selectively. Best free Python course. Bridges syntax to real problem-solving. |
| **☐** | [100 Days of Python — CampusX (Hindi/Urdu)](https://www.youtube.com/playlist?list=PLKnIA16_Rmvb1RYR-iTA_hzfABD8GXSF) | **YouTube** | **◈ SELECTIVE** | Days 1–60. Native-language reinforcement removes cognitive load. Use alongside Bro Code. |

### **1.2 Python OOP (4 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Python OOP Tutorial Series — Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeNtc) | **YouTube** | **▶ WATCH ALL** | Videos 1–6. Classes, inheritance, dunders, properties. Direct prereq for FastAPI and Phase 8. |
| **☐** | [OOP in Python — CampusX (Hindi/Urdu)](https://www.youtube.com/playlist?list=PLKnIA16_RmvbV7HgKPBqoL5VHCXfxMEAJ) | **YouTube** | **◈ SELECTIVE** | Use only if Corey's explanation is unclear. 2 videos. Hindi/Urdu alternative. |

### **1.3 NumPy & Matplotlib (5 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [NumPy Tutorial for Beginners — freeCodeCamp](https://www.youtube.com/watch?v=QUT1VHiLmmI) | **YouTube** | **▶ WATCH ALL** | 1 hr. Fastest path to NumPy fluency. Watch at 1.25×. Arrays, broadcasting, dot product. |
| **☐** | [NumPy Official Docs — Absolute Beginners Guide](https://numpy.org/doc/stable/user/absolute_beginners.html) | **Docs** | **◎ READ** | Reference during first NumPy coding session. Consult alongside the freeCodeCamp video. |
| **☐** | [Matplotlib Tutorial Parts 1–5 — Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeqfco2s763L9E) | **YouTube** | **◈ SELECTIVE** | Parts 1 and 2 are core. Rest optional. Used for Phase 8 benchmark visualisation. |

### **1.4 uv Package Manager — Replace pip and venv entirely (1 day)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [uv Official Documentation — astral.sh/uv](https://docs.astral.sh/uv/) | **Docs** | **◉ READ** | 30-min read. Master: uv init · uv add · uv run · uv sync. Every project starts with uv from Day 1. |
| **☐** | [uv in 5 Minutes — Astral Blog](https://astral.sh/blog/uv) | **Article** | **◎ READ** | Quick-start companion. Read alongside the official docs for context and real-world examples. |

### **1.5 Git & GitHub (1 week)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Git and GitHub for Beginners — Gwen Faraday (freeCodeCamp)](https://www.youtube.com/watch?v=RGOj5yH7evk) | **YouTube** | **▶ WATCH ALL** | 1 hr. Core workflow: commit, branch, push, pull request, merge. Foundation for daily green squares. |
| **☐** | [Learn Git Branching — Interactive Browser Game](https://learngitbranching.js.org/) | **Interactive** | **⚙ PRACTICE** | Introduction + Ramping Up sections (30 min). Hands-on branching — faster than any reading. |

### **1.6 Pydantic V2 (3 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Pydantic V2 Official Documentation](https://docs.pydantic.dev/latest/) | **Docs** | **◉ READ** | BaseModel · @field\_validator · @model\_validator · model\_json\_schema(). Primary reference. |
| **☐** | [Pydantic V2 — ArjanCodes Deep Dive](https://www.youtube.com/watch?v=502XOB0u8OE) | **YouTube** | **◈ SELECTIVE** | Video walkthrough of V2 patterns. Watch if the documentation feels abstract. |

### **1.7 AsyncIO — Most Important Subsection in Phase 1 (1 week)**

|  | **🔴 CRITICAL**  Every production LLM streaming endpoint uses AsyncIO. Synchronous code kills latency under concurrent load. This is the highest-leverage technical skill in the entire foundational stack. |
| --- | --- |

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [AsyncIO in Python — Real Python Guide](https://realpython.com/async-io-python/) | **Article** | **◉ READ** | Focus on tasks, asyncio.gather(), and async generators. The single most important resource in Phase 1. |
| **☐** | [Python Official asyncio Documentation](https://docs.python.org/3/library/asyncio.html) | **Docs** | **◎ READ** | Reference alongside Real Python. async def, await, asyncio.gather(), asyncio.create\_task(). |
| **☐** | [Python Asynchronous Programming — Corey Schafer](https://www.youtube.com/watch?v=t5Bo1Je9EmE) | **YouTube** | **◈ SELECTIVE** | Watch if text-only guides feel slow. Strong visual walkthrough of the event loop model. |

| **PHASE 2** │ **Algorithmic Literacy — Daily NeetCode Routine** |
| --- |
| ⏱ Continuous · 30 min every morning │ ⚙ Core Stack: NeetCode 150 · LeetCode · phase2\_log.md |

Runs parallel to ALL other phases from Day 1. Goal: pattern recognition for the 5 algorithm families in 90% of software engineering interviews. Target: 35–50 problems total. Method: 15-min timer → if stuck, watch NeetCode solution → implement from memory → log.

|  | **⚠ NOTE**  EXCLUDED — Zero ROI for LLM App Engineering: Backtracking · Dynamic Programming · Graph algorithms · Linked Lists · Bit Manipulation · Advanced sorting from scratch. Do not touch these categories. |
| --- | --- |

|  | **✔ DELIVERABLE**  Log format: "Contains Duplicate · hash set · O(n) time · O(n) space" (one line per problem in phase2\_log.md). Sunday: re-solve 3–5 problems from previous weeks. Spaced repetition is more valuable than solving new problems. |
| --- | --- |

### **2.1 Core Resources**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [NeetCode 150 — Practice Platform](https://neetcode.io/practice) | **Platform** | **⚙ PRACTICE** | Solve from the curated list below. 35–50 problems total. Free tier covers everything needed. |
| **☐** | [NeetCode — YouTube Solution Videos](https://www.youtube.com/%40NeetCode) | **YouTube** | **◈ SELECTIVE** | Watch ONLY after a 15-min attempt fails. Implement from memory after — never copy-paste. |

### **2.2 Curated Problem List — 35 to 50 Problems (colour-coded by category)**

| **☐** | **Problem** | **Category** | **Pattern** | **Time** | **Space** | **Done** |
| --- | --- | --- | --- | --- | --- | --- |
| **☐** | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | **Arrays & Hashing** | Hash Set | **O(n)** | **O(n)** | **☐** |
| **☐** | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | **Arrays & Hashing** | Hash Map count | **O(n)** | **O(n)** | **☐** |
| **☐** | [Two Sum](https://leetcode.com/problems/two-sum/) | **Arrays & Hashing** | Hash Map | **O(n)** | **O(n)** | **☐** |
| **☐** | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | **Arrays & Hashing** | Sorted Key Map | **O(nk)** | **O(n)** | **☐** |
| **☐** | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | **Arrays & Hashing** | Bucket Sort / Heap | **O(n)** | **O(n)** | **☐** |
| **☐** | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | **Arrays & Hashing** | Prefix/Suffix Product | **O(n)** | **O(1)** | **☐** |
| **☐** | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | **Arrays & Hashing** | Hash Set per box | **O(1)** | **O(1)** | **☐** |
| **☐** | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | **Arrays & Hashing** | Hash Set | **O(n)** | **O(n)** | **☐** |
| **☐** | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | **Two Pointers** | Two Pointers | **O(n)** | **O(1)** | **☐** |
| **☐** | [Two Sum II — Sorted Input](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | **Two Pointers** | Two Pointers | **O(n)** | **O(1)** | **☐** |
| **☐** | [3Sum](https://leetcode.com/problems/3sum/) | **Two Pointers** | Sort + Two Ptr | **O(n²)** | **O(1)** | **☐** |
| **☐** | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | **Two Pointers** | Greedy Two Ptr | **O(n)** | **O(1)** | **☐** |
| **☐** | [Best Time to Buy/Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | **Sliding Window** | Min Tracker | **O(n)** | **O(1)** | **☐** |
| **☐** | [Longest Substring Without Repeating](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | **Sliding Window** | Set Window | **O(n)** | **O(n)** | **☐** |
| **☐** | [Longest Repeating Char Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | **Sliding Window** | Freq Map Window | **O(n)** | **O(1)** | **☐** |
| **☐** | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | **Stack** | Stack + Map | **O(n)** | **O(n)** | **☐** |
| **☐** | [Min Stack](https://leetcode.com/problems/min-stack/) | **Stack** | Pair Stack | **O(1)** | **O(n)** | **☐** |
| **☐** | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | **Stack** | Stack | **O(n)** | **O(n)** | **☐** |
| **☐** | [Binary Search](https://leetcode.com/problems/binary-search/) | **Binary Search** | Binary Search | **O(log n)** | **O(1)** | **☐** |
| **☐** | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | **Binary Search** | Binary Search | **O(log mn)** | **O(1)** | **☐** |

| **PHASE 3** │ **Dev Environment, Tooling & Model Context Protocol** |
| --- |
| ⏱ 1 week (~15 hours) │ ⚙ Core Stack: Linux CLI · SSH · Cursor / Windsurf · Anthropic MCP |

|  | **★ 2026 NEW**  MCP is the 2026 standard for connecting LLMs to tools and external data. Shipping an MCP server in your GitHub portfolio is an immediate differentiator in 2026 interviews. Build this before any other project. |
| --- | --- |

|  | **✔ DELIVERABLE**  Phase 3 Lab: Build an MCP server with "uv add mcp[cli]". Expose 3 tools: (1) search a local folder by filename pattern, (2) read schema of a SQLite database, (3) query a public weather API. Connect to Cursor or Claude Desktop. Verify all 3 tools invoke correctly with typed responses. |
| --- | --- |

### **3.1 Linux CLI (2 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [50 Most Popular Linux Commands — freeCodeCamp](https://www.youtube.com/watch?v=ZtqBQ68cfJc) | **YouTube** | **◈ SELECTIVE** | Up to File Permissions section only. Commands: cd ls mkdir chmod grep sed awk pipes redirects. |
| **☐** | [Linux Journey — Interactive Learning](https://linuxjourney.com/) | **Interactive** | **⚙ PRACTICE** | Grasshopper + Journeyman sections. Free browser terminal. Muscle memory faster than reading. |

### **3.2 SSH (1 day)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [SSH Crash Course — Traversy Media](https://www.youtube.com/watch?v=hQWRp-FdTpc) | **YouTube** | **▶ WATCH ALL** | 20 min. Key generation, handshakes, port forwarding, scp. Complete coverage in one video. |

### **3.3 Model Context Protocol — MCP (4 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [MCP Official Introduction — modelcontextprotocol.io](https://modelcontextprotocol.io/introduction) | **Docs** | **◉ READ** | Architecture: Hosts, Clients, Servers, Transports, Message types. Read before building anything. |
| **☐** | [MCP Quickstart — Build Your First Server](https://modelcontextprotocol.io/quickstart/server) | **Docs** | **◉ READ** | Step-by-step: build and connect your first MCP server using uv and Python. Follow every step. |
| **☐** | [MCP Python SDK — GitHub](https://github.com/modelcontextprotocol/python-sdk) | **GitHub** | **◎ READ** | Reference SDK. Study the examples/ directory for tool registration and typing patterns. |
| **☐** | [Anthropic MCP Cookbook — Integration Examples](https://github.com/anthropics/anthropic-cookbook) | **GitHub** | **◎ READ** | Code examples for MCP server patterns integrated with Claude Desktop and Claude API. |

| **PHASE 3C** │ **Prompt Engineering Patterns ★ 2026 NEW** |
| --- |
| ⏱ 1 week (~10 hours) │ ⚙ Core Stack: CoT · ReAct · XML Prompts · Few-Shot · Meta-Prompting |

|  | **🔴 CRITICAL**  Read the Anthropic Prompt Engineering docs before writing another prompt in any project. 2 hours of reading permanently raises output quality on every phase after this. The cheapest quality improvement on this entire roadmap. |
| --- | --- |

|  | **✔ DELIVERABLE**  Phase 3C Lab: Create a prompts/ directory with: (1) templates/system\_base.yaml — XML-structured prompt with <role>/<constraints>/<output\_format>/<examples>. (2) loader.py — Pydantic V2 model loading and validating YAML templates. (3) prompt\_optimizer.py — meta-prompting loop: send failing prompt + DeepEval score to Claude, receive rewrite, re-eval, iterate 5 times. Show before/after faithfulness scores in README. |
| --- | --- |

### **3C.1 The 7 Patterns — Learn All, Know When to Use Each**

| **Pattern** | **When to Use** | **Key Implementation Rule** |
| --- | --- | --- |
| **Chain-of-Thought (CoT)** | Multi-step reasoning | Append "Think step by step." or provide 2–3 worked examples. Never use on simple lookups — adds latency with no gain. |
| **ReAct (Reason + Act)** | Any tool-calling agent | Interleave Thought:/Action:/Observation: lines. This is what LangGraph encodes — understand raw text pattern first. |
| **XML System Prompts** | All production prompts | Wrap sections: <role></role> <constraints></constraints> <output\_format></output\_format> <examples></examples>. Claude responds best to XML. |
| **Few-Shot Prompting** | Consistent output format | Include 3–5 input/output examples covering edge cases, not just happy path. Load from JSON, rotate by query type. |
| **Negative Prompting** | Reducing hallucination | Explicit "Do not..." instructions. "Do not invent citations. If uncertain, say: I don't have enough information." Cheapest hallucination fix. |
| **Meta-Prompting** | Prompt optimisation at scale | Send failing prompt + eval score to Claude: "Rewrite to score above 0.85 faithfulness." Build as prompt\_optimizer.py. |
| **Structured Output Prompting** | JSON output required | Never just say "return JSON". Provide exact schema. Use tool\_use (Anthropic) or response\_format (OpenAI). Validate with Pydantic V2. |

### **3C.2 Learning Resources**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Anthropic Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | **Docs** | **◉ READ** | Most important resource in this phase. XML tags, system prompt structure, CoT, anti-patterns. Read fully. |
| **☐** | [DeepLearning.AI — ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) | **Course** | **▶ WATCH ALL** | Free 1-hr course. Best structured intro to CoT, few-shot, and output formats. Start here. |
| **☐** | [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) | **Docs** | **◎ READ** | Reference alongside Anthropic docs. Strategies and tactics section most useful. |
| **☐** | [Brex Prompt Engineering Guide — GitHub](https://github.com/brexhq/prompt-engineering) | **GitHub** | **◎ READ** | Production patterns from a real engineering team. Read Production Prompting and Safety sections. |
| **☐** | [Anthropic Tool Use (Function Calling) Docs](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) | **Docs** | **◉ READ** | Parallel tool calling, tool chaining. Core pattern for all agent development in Phase 9. |
| **☐** | [Instructor — Structured LLM Outputs (Pydantic)](https://github.com/jxnl/instructor) | **GitHub** | **◎ READ** | Pydantic-validated structured outputs from any LLM provider. Works with Anthropic, OpenAI, Gemini. |

| **PHASE 4** │ **Mathematical Intuition & Foundations** |
| --- |
| ⏱ 2 weeks (~20 hours) │ ⚙ Core Stack: 3Blue1Brown · StatQuest · NumPy cosine similarity |

|  | **⚠ NOTE**  Visual intuition only — no heavy problem sets. You need to understand WHY attention works and what cosine similarity means, not derive math from first principles. 3Blue1Brown is the complete approach. Do not touch MIT OCW or any textbook. |
| --- | --- |

|  | **✔ DELIVERABLE**  Phase 4 Lab: Write a pure NumPy script computing Cosine Similarity across a batch of multi-dimensional vectors. Add a pairwise similarity matrix function for N vectors. This exact code appears in your Phase 6 embedding evaluation script — build it here first. |
| --- | --- |

### **4.1 Linear Algebra (4 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Essence of Linear Algebra — 3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | **YouTube** | **◈ SELECTIVE** | Chapters 1–6 ONLY. Vectors, dot products, matrix transforms. Visual foundation for embedding space. |

### **4.2 Calculus (3 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Essence of Calculus — 3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) | **YouTube** | **◈ SELECTIVE** | Chapters 1–5 ONLY. Derivatives and integrals — enough for gradient intuition. No more needed. |

### **4.3 Statistics (3 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Statistics Fundamentals — StatQuest (Josh Starmer)](https://www.youtube.com/%40statquest) | **YouTube** | **◈ SELECTIVE** | First 4 videos + Bayes Theorem video only. Probabilistic reasoning for all eval metrics. |

### **4.4 Neural Network Intuition — Highly Recommended (1 day)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Neural Network from Scratch on MNIST — Samson Zhang](https://www.youtube.com/watch?v=w8yWXqWQYmU) | **YouTube** | **◈ SELECTIVE** | 1-hr NumPy-only code-along. Intuition for weights, gradients, forward pass before Phase 8. |

| **PHASE 5** │ **Structured Engineering & Registry Pipelines** |
| --- |
| ⏱ 2 weeks (~25 hours) │ ⚙ Core Stack: SQL · Pandas · Python Requests · Hugging Face Hub |

SQL lets you query structured metadata alongside vector search. Pandas cleans messy document metadata from real corpora. The Hugging Face Hub is where you push models and datasets to showcase publicly.

|  | **✔ DELIVERABLE**  Phase 5 Lab: (1) Fetch dirty tabular data from a public API using requests. (2) Clean and transform with Pandas — handle missing values, type cast, filter. (3) Write records to local SQLite. (4) Programmatically create and push a model card to Hugging Face Hub with all required metadata fields. |
| --- | --- |

### **5.1 SQL for Data Analytics (4 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [SQL for Data Analytics — Luke Barousse](https://www.youtube.com/watch?v=7mz73uXD9DA) | **YouTube** | **◈ SELECTIVE** | SELECT, JOIN, GROUP BY, CTEs only. These 4 patterns cover 95% of LLM pipeline query needs. |
| **☐** | [Mode SQL Tutorial — Free Interactive Practice](https://mode.com/sql-tutorial/) | **Interactive** | **⚙ PRACTICE** | Free browser SQL environment. Practice Luke's 4 patterns immediately after watching. |
| **☐** | [SQLite Official Documentation](https://www.sqlite.org/docs.html) | **Docs** | **◎ READ** | Reference for Python sqlite3 integration. Connection, cursor, execute, fetchall patterns. |

### **5.2 Pandas (4 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Pandas Complete Tutorial — CampusX (Hindi/Urdu)](https://www.youtube.com/playlist?list=PLKnIA16_RmvbAlyx4_rdtR66B7EHX5k3z) | **YouTube** | **▶ WATCH ALL** | DataFrames, filtering, missing values, groupby. Native language removes cognitive load. |
| **☐** | [Pandas Official Docs — Getting Started](https://pandas.pydata.org/docs/getting_started/index.html) | **Docs** | **◎ READ** | Reference alongside CampusX. Confirm syntax during coding sessions. |

### **5.3 APIs & Web Scraping (3 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Python Requests Tutorial — Corey Schafer](https://www.youtube.com/watch?v=tb8gHvYlCFs) | **YouTube** | **◈ SELECTIVE** | 3 videos: requests + JSON parsing + BeautifulSoup. The complete document scraping stack. |
| **☐** | [httpx Documentation — Async HTTP Client](https://www.python-httpx.org/) | **Docs** | **◎ READ** | Async drop-in for requests. Use in production async pipelines. |

### **5.4 Hugging Face Hub (2 days)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Hugging Face Hub Documentation](https://huggingface.co/docs/hub/index) | **Docs** | **◉ READ** | push\_to\_hub(), model cards, datasets API, private repos. How to version and share all artifacts. |
| **☐** | [Hugging Face Course — Chapter 4: Sharing Models](https://huggingface.co/learn/nlp-course/chapter4/1) | **Course** | **◎ READ** | Free. Model card best practices and metadata fields that make your work discoverable. |

| **PHASE 5B** │ **Document Parsing & Chunking Strategies ★ 2026 NEW** |
| --- |
| ⏱ 1 week (~15 hours) │ ⚙ Core Stack: Unstructured.io · Docling · PyMuPDF · LangChain Splitters |

|  | **🔴 CRITICAL**  Critical prerequisite for Phase 6. In every real enterprise RAG deployment, 80% of engineering time is spent in the ingestion pipeline. Phase 6 is unusable without clean, structured chunks from real documents. |
| --- | --- |

|  | **✔ DELIVERABLE**  Phase 5B Lab: Build an ingestion/ module: (1) parse\_document(path, parser="unstructured") → List[Element] for PDF/DOCX/PPTX. (2) chunk\_document(elements, strategy="recursive") → List[Chunk] with all 4 strategies switchable by config string. (3) ingest\_pipeline.py: parse → chunk → embed → upsert. Log: chunk count, avg tokens, parse time ms, embedding cost USD per run. |
| --- | --- |

### **5B.1 Chunking Strategy Selection — Use the Right One Per Document Type**

| **Strategy** | **Use When** | **Key Settings / Implementation** |
| --- | --- | --- |
| **Recursive Character** | Prose, articles, web content (default) | separators=[\n\n,\n,". "," "] chunk\_size=1024 overlap=100 tokens |
| **Semantic Chunking** | Long technical docs, research papers | Split where sentence cosine similarity drops below threshold. Embed every sentence first. |
| **Parent-Document** | Enterprise RAG default — best recall + context | 128-token chunks for search. 512-token parent chunks returned to LLM. LangChain ParentDocumentRetriever. |
| **Late Chunking** | Legal/financial with long-range dependencies | Embed full document first, pool embeddings per boundary. Jina jina-embeddings-v3 reference impl. |

### **5B.2 Resources**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Unstructured.io Official Documentation](https://docs.unstructured.io/) | **Docs** | **◉ READ** | partition\_pdf(), element types (Title, Table, NarrativeText). strategy="hi\_res" for scanned PDFs. |
| **☐** | [Docling — Quickstart Guide (IBM, open-source 2024)](https://ds4sd.github.io/docling/) | **Docs** | **◉ READ** | PDF → clean Markdown with table structure preserved. Faster than Unstructured. CPU-viable. |
| **☐** | [Docling — GitHub Repository](https://github.com/DS4SD/docling) | **GitHub** | **◎ READ** | Source and examples. Best for financial reports, academic papers, technical standards. |
| **☐** | [PyMuPDF (fitz) — Documentation](https://pymupdf.readthedocs.io/en/latest/) | **Docs** | **◎ READ** | Precise coordinate and block extraction when layout preservation matters exactly. |
| **☐** | [LangChain Parent Document Retriever](https://python.langchain.com/docs/how_to/parent_document_retriever/) | **Docs** | **◉ READ** | Best default for enterprise RAG. Small-to-large retrieval. Study source, reimplement natively. |
| **☐** | [Jina Late Chunking — Research Blog](https://jina.ai/news/late-chunking-in-long-context-embedding-models/) | **Article** | **◎ READ** | Theory and implementation. Full-doc embedding before boundary pooling. For long-range deps. |

| **PHASE 6** │ **Vector Processing, Redis Caching & Hybrid Retrieval** |
| --- |
| ⏱ 3 weeks (~51 hours) │ ⚙ Core Stack: Qdrant · Redis VSS · BM25 · FlashRank · RRF · Embedding Eval |

Naive vector search alone fails on exact queries — a user searching "GDPR Article 17" gets semantically similar but not precisely matching chunks. The solution is hybrid search: dense + sparse combined via Reciprocal Rank Fusion, then cross-encoder reranked. This is the 2026 enterprise RAG standard.

|  | **✔ DELIVERABLE**  Phase 6 Lab: (1) Run embedding\_eval.py — benchmark 3+ models on a 20-question gold set, pick the winner for your domain. (2) Ingest real document corpus → chunk (Phase 5B pipeline) → embed → index in Qdrant. (3) Implement concurrent dense + BM25 search. (4) Merge with RRF. (5) Rerank top-20 → top-5 with FlashRank. (6) Cache results in Redis. Report Recall@5 in README. |
| --- | --- |

### **6.1 Embedding Model Selection — Evaluate Before You Build**

|  | **⚠ NOTE**  Wrong embedding model = 20–30% Recall@5 drop on your domain. Start with nomic-embed-text locally (free on RTX 4060). Run evaluation\_eval.py on your actual corpus. Then decide on cloud model if needed. |
| --- | --- |

| **Model** | **Dimensions** | **Cost / 1K** | **Speed** | **Best For** |
| --- | --- | --- | --- | --- |
| **text-embedding-3-small (OpenAI)** | **1536** | **$0.00002** | **120ms** | General English enterprise docs. Cheapest cloud option. Good default when budget is tight. |
| **embed-english-v3.0 (Cohere)** | **1024** | **$0.0001** | **140ms** | Highest retrieval accuracy. Asymmetric: separate document vs query embedding types. |
| **nomic-embed-text (Ollama / local)** | **768** | **$0 free** | **8ms** | Privacy-sensitive data. Competitive on general text. Use for ALL local development. |
| **mxbai-embed-large (Ollama / local)** | **1024** | **$0 free** | **12ms** | Best local quality. RTX 4060 compatible (~2GB VRAM). Use for production-like local tests. |

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Fireship — Vectors and Embeddings in 10 Minutes](https://www.youtube.com/watch?v=ySus5ZS0b94) | **YouTube** | **▶ WATCH ALL** | Best first introduction to embeddings and vector spaces. Watch before anything else in Phase 6. |
| **☐** | [DeepLearning.AI — Vector Databases & Embeddings (Free)](https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/) | **Course** | **▶ WATCH ALL** | Free short course. Embeddings, indexing, retrieval. Best structured foundation for this phase. |
| **☐** | [MTEB Leaderboard — Hugging Face](https://huggingface.co/spaces/mteb/leaderboard) | **Platform** | **◎ READ** | Benchmark rankings. Filter by retrieval task and language. Supplement your domain-specific eval. |
| **☐** | [Ollama Embedding Models Guide](https://ollama.com/blog/embedding-models) | **Docs** | **◉ READ** | nomic-embed-text and mxbai-embed-large. Pull and serve locally. Free on your RTX 4060. |

### **6.2 Vector Stores**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Qdrant Quickstart — Official Documentation](https://qdrant.tech/documentation/quickstart/) | **Docs** | **◉ READ** | Local + Qdrant Cloud setup. Collections, upsert, vector search, payload filtering. Primary vector store. |
| **☐** | [Qdrant Python Client Documentation](https://python-client.qdrant.tech/) | **Docs** | **◎ READ** | Full API reference. QdrantClient, PointStruct, SearchRequest, filter patterns. |
| **☐** | [pgvector — GitHub Repository](https://github.com/pgvector/pgvector) | **GitHub** | **◎ READ** | PostgreSQL vector extension. Use when you need SQL queries alongside vector search. |
| **☐** | [Redis VSS — Vector Similarity Search Docs](https://redis.io/docs/stack/search/reference/vectors/) | **Docs** | **◉ READ** | Semantic caching layer. Vector similarity, approximate nearest neighbor, TTL management. |

### **6.3 Hybrid RAG Pipeline — BM25 + Dense + RRF + Reranking**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [rank\_bm25 — GitHub Repository](https://github.com/dorianbrown/rank_bm25) | **GitHub** | **◉ READ** | BM25 implementation. Index corpus → score queries → ranked results. The sparse retrieval component. |
| **☐** | [LangChain EnsembleRetriever — Documentation](https://python.langchain.com/docs/how_to/ensemble_retriever/) | **Docs** | **◉ READ** | Combine BM25 + dense retriever. Weights parameter for tuning the hybrid balance. |
| **☐** | [FlashRank — Cross-Encoder Reranking](https://github.com/PrithivirajDamodaran/FlashRank) | **GitHub** | **◉ READ** | Local reranking. top-20 → top-5. Runs on CPU, no API key, pip install flashrank. |
| **☐** | [RRF Original Paper — Cormack et al. 2009](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) | **Paper** | **◎ READ** | Read the formula section only. Implementation is 10 lines of Python. Understand before building. |

| **PHASE 7** │ **Production API · Eval CI/CD · Security · Context Management** |
| --- |
| ⏱ 5 weeks (~89 hours) │ ⚙ Core Stack: FastAPI · Docker · DeepEval · GitHub Actions · Guardrails AI · LLMLingua |

|  | **🔴 CRITICAL**  EVAL-FIRST LAW: No prompt modification ships without a passing automated test suite. CI must block merge on every push if Faithfulness < 0.85, Answer Relevancy < 0.80, or Hallucination > 0.15. This is the #1 differentiator between a demo builder and a production engineer. |
| --- | --- |

|  | **✔ DELIVERABLE**  Phase 7 Lab: Containerized FastAPI app with (1) /chat/stream SSE async streaming endpoint, (2) GitHub Actions CI running DeepEval on every push blocking merge on threshold violations, (3) Security middleware — injection detection + rate limiting (20 req/min per IP), (4) Token budget enforcement with tiktoken before every LLM call, (5) Guardrails AI validation on all outputs. All CI gates must be green. |
| --- | --- |

| **Eval Metric** | **Threshold** | **Blocks Merge?** | **Tool** |
| --- | --- | --- | --- |
| **Faithfulness** | **≥ 0.85** | **YES — CI FAILS** | DeepEval FaithfulnessMetric |
| **Answer Relevancy** | **≥ 0.80** | **YES — CI FAILS** | DeepEval AnswerRelevancyMetric |
| **Hallucination** | **≤ 0.15** | **YES — CI FAILS** | DeepEval HallucinationMetric |
| **Contextual Recall** | **≥ 0.75** | **Warning only** | DeepEval ContextualRecallMetric |

### **7.1 FastAPI Async Streaming (1.5 weeks)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [FastAPI Official Tutorial — Tiangolo](https://fastapi.tiangolo.com/tutorial/) | **Docs** | **◉ READ** | Async routes, Pydantic models, dependency injection, background tasks. Primary reference. |
| **☐** | [FastAPI Full Course — freeCodeCamp](https://www.youtube.com/watch?v=0sOvCWFmrtA) | **YouTube** | **◈ SELECTIVE** | Video walkthrough. Watch alongside official docs if text-only feels slow. |
| **☐** | [MDN — Server-Sent Events Reference](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) | **Docs** | **◎ READ** | SSE protocol. Understand text/event-stream format for token streaming. |

### **7.2 Docker & Containerisation (1 week)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Docker Tutorial for Beginners — TechWorld with Nana](https://www.youtube.com/watch?v=3c-iBn73dDE) | **YouTube** | **◈ SELECTIVE** | 3 hrs total — watch multi-stage builds and docker-compose sections. Skip Docker Hub push. |
| **☐** | [Docker Official Docs — Getting Started](https://docs.docker.com/get-started/) | **Docs** | **◎ READ** | Dockerfile syntax, multi-stage builds, .dockerignore, environment variables. |

### **7.3 Eval-First CI/CD Pipeline (1 week)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [DeepEval Official Documentation](https://docs.confident-ai.com/) | **Docs** | **◉ READ** | FaithfulnessMetric, AnswerRelevancyMetric, HallucinationMetric. CI integration. Primary eval framework. |
| **☐** | [GitHub Actions Official Documentation](https://docs.github.com/en/actions) | **Docs** | **◉ READ** | Workflow YAML syntax, CI gates, secrets management. Build .github/workflows/eval.yml here. |
| **☐** | [Promptfoo — Documentation](https://www.promptfoo.dev/docs/intro/) | **Docs** | **◎ READ** | Alternative eval for A/B testing system prompts and red-teaming your application. |
| **☐** | [pytest + pytest-asyncio — Documentation](https://docs.pytest.org/en/stable/) | **Docs** | **◎ READ** | pytest-asyncio for testing async FastAPI endpoints. Unit tests for every component. |

### **7.4 Security & Guardrails ★ NEW**

|  | **🔴 CRITICAL**  Production LLM apps are attacked via prompt injection from day one. This module is the clearest signal interviewers use in 2026 to distinguish demo builders from production engineers. |
| --- | --- |

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [OWASP LLM Top 10 — Security Risks 2025](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | **Docs** | **◉ READ** | All 10 LLM security risks. Prompt injection, insecure output, data poisoning. Read every entry. |
| **☐** | [Guardrails AI — Official Documentation](https://www.guardrailsai.com/docs) | **Docs** | **◉ READ** | Guards + validators: ValidJson, DetectSecrets, ToxicLanguage. Wrap every LLM call. |
| **☐** | [slowapi — Rate Limiting for FastAPI](https://github.com/laurentS/slowapi) | **GitHub** | **◉ READ** | Per-IP: 20 req/min. Per-user: 100 req/hr. Returns 429 with Retry-After header on violation. |
| **☐** | [Anthropic Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) | **Docs** | **◎ READ** | Model provider safety perspective. Important context for building responsible systems. |

### **7.5 Context Window Management ★ NEW (Light version — 2 hours)**

|  | **⚠ NOTE**  Light version only: add token counting + hard chunk limit now. Add LLMLingua only when real throughput data shows cost is the bottleneck. |
| --- | --- |

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Tiktoken — Token Counting (OpenAI / LiteLLM)](https://github.com/openai/tiktoken) | **GitHub** | **◉ READ** | Count tokens before every LLM call. Enforce hard input limits. Prevents cost attacks. |
| **☐** | [Anthropic Token Counting API](https://docs.anthropic.com/en/docs/build-with-claude/token-counting) | **Docs** | **◉ READ** | client.count\_tokens(messages=messages). Exact count before billing. Add to every Anthropic call. |
| **☐** | [LLMLingua — Prompt Compression (Microsoft)](https://github.com/microsoft/LLMLingua) | **GitHub** | **◎ READ** | 3–5× compression, <5% accuracy loss. Apply to retrieved chunks when over budget. Defer until scale. |

| **PHASE 8** │ **Deep Learning Internals & Open-Source Serving** |
| --- |
| ⏱ 3 weeks (~45 hours) │ ⚙ Core Stack: Karpathy Series · Ollama · vLLM · unsloth + QLoRA · Benchmarking |

This phase gives you the internals knowledge that separates a capable engineer from one just calling APIs. Understanding BPE tokenization directly explains why context limits exist, why prefix caching saves money, and why some prompts cost more than others.

|  | **🔴 CRITICAL**  Code every single line of both Karpathy videos. Do not just watch. The BPE tokenizer section alone explains context limits, token pricing, and prefix caching — all critical for cost control in Phase 10. |
| --- | --- |

|  | **✔ DELIVERABLE**  Phase 8 Lab: Benchmark table with 4 models (e.g. Phi-4, Llama-3.2-3B, Qwen-3, + 1 cloud API). Columns: Tokens/sec · Peak VRAM GB · Cost per 1K tokens · Accuracy rating. Visualise with matplotlib. Proves you understand the cost-quality frontier every company optimises. |
| --- | --- |

### **8.1 Karpathy LLM Series — Code Every Line (2 weeks)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Let's Build GPT from Scratch — Andrej Karpathy](https://www.youtube.com/watch?v=kCc8FmEb1nY) | **YouTube** | **▶ WATCH ALL** | 2 hrs. Self-attention, transformers, forward pass. Code every line. Best ML video ever made. |
| **☐** | [Let's Build the GPT Tokenizer — Andrej Karpathy](https://www.youtube.com/watch?v=zduSFxRajkE) | **YouTube** | **▶ WATCH ALL** | 2 hrs. BPE algorithm, merge rules, prefix caching. Explains token pricing and context limits directly. |
| **☐** | [Neural Networks: Zero to Hero — Full Playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | **YouTube** | **◈ SELECTIVE** | makemore and nanoGPT videos most relevant. Watch for deeper intuition beyond the two core videos. |

### **8.2 Local Model Serving (1 week)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Ollama — Official Site & Installation](https://ollama.com/) | **Tool** | **⚙ PRACTICE** | Install. Pull Llama-3.2-3B, Phi-4, Qwen-3. Run OpenAI-compatible API server. Run Phase 8 benchmark. |
| **☐** | [Ollama Model Library](https://ollama.com/library) | **Platform** | **◎ READ** | All available models with VRAM requirements. Filter by RTX 4060 8GB VRAM budget. |
| **☐** | [vLLM Documentation — OpenAI-Compatible Server](https://docs.vllm.ai/en/latest/) | **Docs** | **◉ READ** | Paged attention for production throughput. OpenAI-compatible API. For high-load serving. |
| **☐** | [unsloth — QLoRA Fine-Tuning (RTX 4060 compatible)](https://github.com/unslothai/unsloth) | **GitHub** | **◎ READ** | Run ONCE for intuition — QLoRA adapters, quantisation tradeoffs, VRAM constraints. Not for production. |

| **PHASE 9** │ **Stateful Multi-Agent Graph Engineering & Memory Architecture** |
| --- |
| ⏱ 4 weeks (~68 hours) │ ⚙ Core Stack: LangGraph · Claude Extended Thinking · Langfuse · Memory Systems |

LangGraph provides cyclic state machines where agents loop, branch, and escalate — far beyond linear chains. Memory architecture is the critical 2026 addition: agents without proper memory fail within their first real multi-turn conversation. Implement all three memory types.

|  | **✔ DELIVERABLE**  Phase 9 Lab: LangGraph state machine that (1) fetches prompts from Langfuse at runtime, (2) routes simple tasks to Gemini 2.5 Flash, (3) routes complex reasoning to Claude with budget\_tokens, (4) implements all 3 memory types, (5) traces every node in Langfuse with span-level detail. Demonstrate that a preference from session 1 applies automatically in session 5. |
| --- | --- |

### **9.1 LangGraph State Machines (1.5 weeks)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [LangGraph Official Documentation](https://langchain-ai.github.io/langgraph/) | **Docs** | **◉ READ** | State machines, TypedDict state, nodes, conditional edges, persistence. Primary reference. |
| **☐** | [LangGraph Academy — Intro to LangGraph (Free)](https://academy.langchain.com/courses/intro-to-langgraph) | **Course** | **▶ WATCH ALL** | Official free course. Most comprehensive walkthrough. Start here before the docs. |
| **☐** | [LangGraph — Human-in-the-Loop Guide](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/) | **Docs** | **◉ READ** | Interrupt nodes, approval flows. The Slack webhook intercept pattern for confidence < 70%. |

### **9.2 Reasoning Models (0.5 weeks)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Anthropic Extended Thinking Documentation](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) | **Docs** | **◉ READ** | budget\_tokens parameter, when to enable extended thinking, cost vs quality tradeoffs. |
| **☐** | [OpenAI Reasoning Models Guide (o3/o4)](https://platform.openai.com/docs/guides/reasoning) | **Docs** | **◎ READ** | reasoning\_effort: low/medium/high. When to use o-series vs cheaper models in your router. |

### **9.3 Prompt Registry & Observability (0.5 weeks)**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Langfuse Official Documentation](https://langfuse.com/docs) | **Docs** | **◉ READ** | Tracing, prompt management, cost tracking, eval scores, user sessions. Core observability tool. |
| **☐** | [Langfuse Prompt Management Guide](https://langfuse.com/docs/prompts/get-started) | **Docs** | **◉ READ** | Version prompts, fetch at runtime, A/B test variants. The dynamic prompt registry pattern. |

### **9.4 Memory Architecture for Agents ★ NEW (1 week)**

|  | **★ 2026 NEW**  All 3 memory types required for production agents. Short-term only = repetitive responses. Long-term only = no session coherence. Episodic only = no preference learning. Implement all three. |
| --- | --- |

| **Memory Type** | **Storage** | **Scope** | **Implementation** |
| --- | --- | --- | --- |
| **Short-term** | **In-memory list** | Current session | Keep last K messages. Summarise overflow using Gemini Flash (cheap). Prevents unbounded context. |
| **Long-term** | **Qdrant vector store** | Cross-session persistent | Extract facts at session end → embed → store. Retrieve at session start with first message as query. |
| **Episodic** | **Redis + TTL** | Task-scoped 24hr | Log every tool call + result. Never repeat a failed strategy with identical params. Auto-expires. |

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [LangChain Conversation Memory — Chatbots Guide](https://python.langchain.com/docs/how_to/chatbots_memory/) | **Docs** | **◉ READ** | Short-term buffer with auto-summarisation. Study source, then reimplement natively in LangGraph. |
| **☐** | [LangGraph Persistence — Checkpointers](https://langchain-ai.github.io/langgraph/concepts/persistence/) | **Docs** | **◉ READ** | State persistence across runs. Foundation for cross-session long-term memory architecture. |
| **☐** | [Langfuse Tracing Documentation](https://langfuse.com/docs/tracing) | **Docs** | **◉ READ** | Trace every agent node, span every tool call. Observability layer for debugging memory issues. |
| **☐** | [Redis Keyspace — TTL & Expiry](https://redis.io/docs/manual/keyspace-notifications/) | **Docs** | **◎ READ** | TTL for episodic memory. Task-scoped stores that auto-expire after 24 hours. |

| **PHASE 10** │ **Production Capstone — High-Throughput Enterprise Answer Engine** |
| --- |
| ⏱ 4 weeks (~60 hours) │ ⚙ Core Stack: LiteLLM · LangGraph · Langfuse · Railway · All Phase 1–9 components |

|  | **🔴 CRITICAL**  Primary portfolio project. Recruiters will read this codebase. Every function must be typed, async, tested, and documented. Eval CI must be green on every single commit. This is not a prototype — it is a production-grade system. |
| --- | --- |

Architecture: User JSON → FastAPI Async Loop → Redis Semantic Cache (hit → instant return) → LangGraph Router

* Simple task branch: Gemini 2.5 Flash (low cost, fast)
* Complex task branch: Claude Extended Thinking → Confidence check → Slack webhook if < 70% (Human-in-the-Loop)
* /dashboard/costs → LiteLLM Spend API → real-time per-model cost data

### **10.1 Week 1 — FastAPI + Redis Cache + Pydantic Validation**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [LiteLLM Official Documentation](https://docs.litellm.ai/) | **Docs** | **◉ READ** | Proxy setup, model routing (cheap vs reasoning), spend tracking API for /dashboard/costs. |
| **☐** | [LiteLLM GitHub Repository](https://github.com/BerriAI/litellm) | **GitHub** | **◎ READ** | Configuration examples, cost tracking patterns, provider fallbacks and retry logic. |

### **10.2 Week 2 — Hybrid Retrieval Integration**

Wire Phase 6 engine into FastAPI: Qdrant/pgvector dense + BM25 + RRF + FlashRank. Add Redis semantic cache (threshold 0.92). Cache hit rate target: > 30%.

### **10.3 Week 3 — LangGraph + Langfuse + Model Router**

Integrate Phase 9 LangGraph agent. Langfuse prompt registry for runtime template fetch. Query classifier: token count < 500 and low entropy → Gemini Flash. Otherwise → Claude Extended Thinking with budget\_tokens=8000.

### **10.4 Week 4 — Human-in-the-Loop + Cost Dashboard + Final CI**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Railway — Free Deployment Platform](https://railway.app/) | **Platform** | **⚙ PRACTICE** | Docker deployment. Environment variables. Free tier. Deploy here for a live demo URL in portfolio. |
| **☐** | [Render — Alternative Free Deployment](https://render.com/) | **Platform** | **◎ READ** | Alternative to Railway. Free web service tier for FastAPI containers. |
| **☐** | [Slack API — Incoming Webhooks](https://api.slack.com/messaging/webhooks) | **Docs** | **◉ READ** | Webhook for human-in-the-loop escalation node. Fires when agent confidence < 70%. |

|  | **✔ DELIVERABLE**  Final Capstone Checklist — tick every item before calling Phase 10 complete:  ☐ FastAPI /chat/stream SSE endpoint ☐ Redis semantic cache ☐ Hybrid RAG (BM25+dense+RRF+FlashRank)  ☐ LangGraph state machine ☐ Langfuse prompt registry ☐ Gemini Flash / Claude routing  ☐ Slack webhook human-in-the-loop ☐ /dashboard/costs endpoint ☐ Security middleware (injection + rate limit)  ☐ Eval CI green on every push ☐ Deployed to Railway with live URL ☐ README with full architecture diagram |
| --- | --- |

| **PHASE 11** │ **Interview Prep — LLM System Design** |
| --- |
| ⏱ 2 weeks parallel to Phase 10 (~10 hours) │ ⚙ Core Stack: 5 Design Questions · Scripted spoken answers · 4-min practice sessions |

|  | **⚠ NOTE**  Run parallel to Phase 10. 30 min/day alongside morning NeetCode. Practice speaking answers aloud, timed. Notes alone are insufficient — the value is in fluent delivery. |
| --- | --- |

### **11.1 The 5 System Design Questions — Prepare All Five**

| **Q** | **System Design Question** | **Scripted Answer Structure (practice aloud 4–5 min)** |
| --- | --- | --- |
| **Q1** | **Design a RAG system for 10 million documents.** | Ingestion pipeline → chunking strategy per doc type → embedding eval (show Recall@5) → Qdrant HNSW sharded → hybrid BM25+dense+RRF → FlashRank reranking → Redis semantic cache → FastAPI streaming. State: Recall@5 > 85%, P50 < 500ms, cost per query $X. |
| **Q2** | **How would you cut LLM API costs by 50%?** | 5-layer stack: (1) Semantic caching — 30–40% hit rate. (2) Model routing — Flash for simple, Claude for complex. (3) LLMLingua on chunks — 3–5× compression. (4) Batch inference — 50% discount for async jobs. (5) Prefix caching — static context first, saves 40–60% on repeated prefixes. Combined: 55–70% realistic reduction. |
| **Q3** | **How do you evaluate an LLM app in production?** | 3 layers: (1) Offline evals — DeepEval gates block every deploy that fails thresholds. (2) Online sampling — 2–5% of production calls, async eval worker, scores to Langfuse. (3) Human feedback — weekly review of 50 flagged responses. Drift detection: alert when 7-day rolling faithfulness drops > 0.05. |
| **Q4** | **Walk through debugging a hallucinating RAG system.** | Framework: (1) Run Recall@5 on gold set — < 80% means fix retrieval, not generation. (2) Check chunk quality — is answer inside top-5 chunks? (3) Run faithfulness scorer — model going beyond context? (4) Add negative prompt constraints. (5) Try stronger model for hard reasoning tasks. |
| **Q5** | **How do you make an LLM agent production-reliable?** | 7 layers: Human-in-the-loop for low-confidence irreversible actions + idempotent tool design (upsert not insert) + exponential backoff retry (1s/2s/4s, max 3) + episodic memory (no repeated failed strategies) + full Langfuse span tracing + sandboxed code execution + graceful degradation (partial answer beats confident hallucination). |

### **11.2 Resources**

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [NeetCode — System Design Playlist](https://www.youtube.com/%40NeetCodeIO) | **YouTube** | **◈ SELECTIVE** | General system design fundamentals. Supplement with LLM-specific patterns from your capstone. |
| **☐** | [Anthropic Full Documentation](https://docs.anthropic.com/) | **Docs** | **◎ READ** | Review all APIs you have used. Technical depth questions come directly from here. |

| **PHASE 12** │ **Portfolio Website — Final Packaging Step** |
| --- |
| ⏱ 1 weekend (~8 hours) │ ⚙ Core Stack: Astro · Cloudflare Pages · Vercel · 1 Technical Post |

|  | **⚠ NOTE**  Build AFTER all 3 projects exist. This is packaging, not learning. Ship before the first job application. Zero portfolio = lost interview conversions. |
| --- | --- |

|  | **✔ DELIVERABLE**  Checklist before sending first application:  ☐ Live URL deployed to Cloudflare Pages or Vercel (free) ☐ Hero with positioning statement + GitHub/LinkedIn/email  ☐ Exactly 3 projects with real metrics (Recall@5, P50ms, cache hit %, cost per query)  ☐ Skills matrix: Languages · Frameworks · Vector Stores · Eval Tools · Models · Deployment  ☐ 1 technical blog post (800+ words, code snippet, before/after metrics) ☐ URL on resume + LinkedIn + GitHub profile |
| --- | --- |

|  | **💡 TIP**  "I build production RAG systems, streaming AI APIs, and cost-optimised multi-agent pipelines." — Refine this as your positioning statement. 3 projects: Hybrid RAG Engine (Ph6) · FastAPI Eval CI App (Ph7) · Enterprise Answer Engine (Ph10). |
| --- | --- |

| **☐** | **Resource** | **Platform** | **Badge** | **Notes** |
| --- | --- | --- | --- | --- |
| **☐** | [Astro — Static Site Generator Documentation](https://docs.astro.build/en/getting-started/) | **Docs** | **◉ READ** | Best framework for a portfolio site. Zero JS default, fast, deploys from GitHub in 30 seconds. |
| **☐** | [Cloudflare Pages — Free Deployment](https://developers.cloudflare.com/pages/) | **Docs** | **◉ READ** | Free tier, auto HTTPS, custom domain. Connect GitHub repo, deploy automatically on every push. |
| **☐** | [Vercel — Alternative Free Deployment](https://vercel.com/docs) | **Docs** | **◎ READ** | Alternative to Cloudflare Pages. Both free for static sites. Choose either. |

| **Daily & Weekly Execution Routine** |
| --- |

| **Day** | **Time** | **Activity** |
| --- | --- | --- |
| **Every Morning** | **30 min** | Solve 1 NeetCode problem. 15-min timer → watch solution if stuck → implement from memory → log in phase2\_log.md with pattern and complexity. Never skip this habit. |
| **Mon / Wed / Fri** | **1.5–2 hrs** | Course study for active phase (4–10). Watch at 1.25×–1.5×. Take notes in code files, not text documents. Every concept gets a .py file. |
| **Tue / Thu** | **1.5–2 hrs** | Project coding: RAG prototypes, MCP server improvements, FastAPI endpoints, eval pipeline. Code, commit, push. Green squares every single day. |
| **Saturday** | **2–3 hrs** | Portfolio project: capstone work, deployment, architecture documentation, README. Longest session of the week. |
| **Sunday** | **30–45 min** | Spaced repetition: re-solve 3–5 NeetCode problems from previous weeks. Update progress\_log.md — what worked, what struggled, next week plan. |
| **Exam Weeks** | **Minimum** | 1 LeetCode problem (30 min) + 1 uv/CLI command practiced. No new courses. Preserve the daily commit habit above everything else. |

| **Absolute Exclusions — Do Not Touch** |
| --- |

|  | **🔴 CRITICAL**  Every hour spent on these topics is an hour not spent on RAG, agents, evals, and streaming. The opportunity cost directly delays your job timeline. |
| --- | --- |

| **🚫 Topic / Tool** | **Why Excluded — Full Reasoning** |
| --- | --- |
| **Classical ML — XGBoost, scikit-learn, Kaggle** | Zero relevance to LLM APIs, RAG, and agents. Entirely disjoint skill set from LLM Application Engineering. |
| **Andrew Ng ML Specialisation (Coursera)** | Built for ML researchers. Decision trees, SVMs, gradient descent proofs — none appear in LLM app engineering. |
| **DVC · Prefect · Parquet** | Data engineering for training pipelines. You ingest documents (KB–MB), not terabyte feature stores. |
| **Feast — Feature Stores** | 100% classical ML tooling. No use case in LLM application engineering whatsoever. |
| **Kubernetes (K8s)** | Railway/Render/Fly.io abstract this completely. Learn only if a JD explicitly requires K8s. |
| **Backtracking · DP · Graph algorithms** | Not in LLM app engineering interviews or codebases. Your 35–50 NeetCode target is sufficient. |
| **Diffusion Models (Stable Diffusion)** | Entirely separate skill tree. Add only if a JD explicitly requires image generation. |
| **Voice AI — real-time STT/TTS** | Niche specialisation with a completely separate stack. Target only for voice-specific roles. |
| **Apache Spark / PySpark** | Distributed computing for terabytes. You process documents (KB–MB), not data lakes. |
| **MLflow — Experiment Tracking** | Built for classical ML training runs. Langfuse is purpose-built and superior for LLM observability. |
| **Weights & Biases Sweeps** | Training experiment tracker. Zero use case in LLM application engineering. Langfuse replaces this. |
| **TensorFlow / Keras** | Use NumPy + Karpathy for neural network intuition. TF adds 2 weeks overhead for zero gain. |
| **AWS ML Specialty / GCP ML Cert** | 3–6 month prep tracks for SageMaker/Vertex AI. Wrong signal, wrong tools, massive time cost. |
| **LangChain LCEL as a destination** | Linear chains break in production. LangGraph is the destination. LCEL is a stepping stone only. |
| **Celery — Distributed Task Queue** | Overengineered for most LLM apps. Use asyncio.create\_task() or ARQ (lightweight async Redis queue). |
| **WebSockets as primary transport** | SSE (Phase 7) is correct for one-direction token streaming. WebSockets add bidirectional complexity. |
| **Scrapy — Web Scraping Framework** | Use requests + BeautifulSoup (Phase 5) or crawl4ai for LLM-native scraping. Scrapy adds steep overhead. |
| **AutoML — AutoKeras, H2O, Ludwig** | Automates classical ML model selection. No intersection with LLM application engineering. |

| **Stop planning. Start executing.**  Phase 1 → uv init → AsyncIO lab → git commit → git push  *A focused plan executed completely beats an infinite plan started repeatedly.*  Muhammad Abdurrehman Azam · USTB · 2025–2028 · LLM Application Engineer |
| --- |

