<div align="center">
  <img src="https://avatars.githubusercontent.com/u/81901376?v=4" width="120" style="border-radius:50%; border: 2px solid #30363d;"><br/>
  <h1>🚀 Production LLM Engineer Track</h1>
  <p><b>36‑Month Curriculum & Audit Trail (2025–2028)</b></p>

  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="License"/></a>
  <img src="https://img.shields.io/github/last-commit/AbdurrehmanAzam/production-llm-engineer-track?color=success&style=flat-square" alt="Last Commit"/>
  <br/><br/>
  <img src="https://img.shields.io/badge/Phase%201-✅%20Complete-brightgreen?style=flat-square" alt="Phase 1"/>
  <img src="https://img.shields.io/badge/Phase%202-🔄%20Active-blue?style=flat-square" alt="Phase 2"/>
  <img src="https://img.shields.io/badge/German%20A2-📖%20In%20Progress-yellow?style=flat-square" alt="German A2"/>
</div>

---

## 📋 Executive Summary
This repository serves as a **transparent, reproducible audit trail** mapping a transition from software engineering foundations to a **Production LLM Application Engineer**. The curriculum strictly follows Track A (LLM Engineering) and explicitly bypasses classical ML and MLOps components irrelevant to modern generative AI application development.

| Area | Focus |
| :--- | :--- |
| **Role** | LLM Engineer, AI Application Engineer |
| **Target** | M.Sc. in AI / Data Science (Germany, 2028) |
| **Methodology** | 100% open‑source, reproducible environments, test-driven production |

---

## 🛠️ Technology Stack

| Category | Tools |
| :--- | :--- |
| **Languages** | Python 3.12, C++ |
| **Core Computing** | NumPy, Matplotlib |
| **Infrastructure** | Linux (WSL2), uv, Git/GitHub, Docker |
| **AI/LLM Primitives** | FastAPI, Qdrant, LangGraph, vLLM, DeepEval |

---

## 🗺️ Architectural Roadmap (Phase 0–12)

| Phase | Module | Status |
| :---: | :--- | :---: |
| **00** | **Foundation:** uv, Git, WSL2, Cursor | ⏳ |
| **01** | **Python for LLM:** AsyncIO, Pydantic V2, Type Hints, Context Managers | 🔄 |
| **02** | **DSA:** 37 NeetCode Problems | ⏳ |
| **03** | **Dev & MCP:** Linux, SSH, Free Inference (Groq/AI Studio), MCP | ⏳ |
| **03C** | **Prompt Engineering:** CoT, ReAct, XML, Few-Shot, Meta-Prompting | ⏳ |
| **04** | **Math:** 3Blue1Brown, StatQuest, NumPy Cosine Similarity | ⏳ |
| **05** | **Data Engineering:** SQL, Pandas, APIs, Hugging Face Hub | ⏳ |
| **05B** | **Parsing & Chunking:** Docling, Unstructured, LangChain Splitters | ⏳ |
| **06** | **Hybrid RAG:** Qdrant, Redis, BM25, FlashRank, RRF | ⏳ |
| **07** | **FastAPI & Evals:** FastAPI, Docker, DeepEval, GitHub Actions, Guardrails | ⏳ |
| **08** | **LLM Internals:** Karpathy Series, Ollama, vLLM, unsloth | ⏳ |
| **09** | **Multi-Agent:** LangGraph, Pydantic AI, Langfuse, Memory Systems | ⏳ |
| **10** | **Capstone:** Enterprise Answer Engine (LiteLLM + LangGraph + Railway) | ⏳ |
| **11** | **Interview Prep:** 5 System Design Questions | ⏳ |
| **12** | **Portfolio:** Astro, Cloudflare Pages / Vercel | ⏳ |

> 📘 **Detailed phase logs** are maintained in the `phases/` directory.

---

## 🚀 Local Setup

    # Clone the repository
    git clone https://github.com/AbdurrehmanAzam/production-llm-engineer-track.git
    cd production-llm-engineer-track

    # Sync the deterministic environment
    uv sync

    # Run execution
    uv run <script_name>.py
