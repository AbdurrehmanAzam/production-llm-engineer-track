<div align="center">
  <img src="https://avatars.githubusercontent.com/u/81901376?v=4" width="120" style="border-radius:50%; border: 2px solid #30363d;"><br/>
  <h1>🚀 Production LLM Engineer Track</h1>
  <p><b>36‑Month Curriculum & Audit Trail (2025–2028)</b></p>

  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="License"/></a>
  <img src="https://img.shields.io/github/last-commit/AbdurrehmanAzam/production-llm-engineer-track?color=success&style=flat-square" alt="Last Commit"/>
  <img src="https://img.shields.io/github/issues/AbdurrehmanAzam/production-llm-engineer-track?color=blue&style=flat-square" alt="Issues"/>
  <img src="https://img.shields.io/github/stars/AbdurrehmanAzam/production-llm-engineer-track?color=yellow&style=flat-square" alt="Stars"/>
  <br/><br/>
  <img src="https://img.shields.io/badge/Phase%201-✅%20Complete-brightgreen?style=flat-square" alt="Phase 1"/>
  <img src="https://img.shields.io/badge/Phase%202-🔄%20Active-blue?style=flat-square" alt="Phase 2"/>
  <img src="https://img.shields.io/badge/German%20A2-📖%20In%20Progress-yellow?style=flat-square" alt="German A2"/>
</div>

---

## 📋 Executive Summary
This repository is a **transparent, reproducible audit trail** of my transition from software engineering foundations to a **Production LLM Application Engineer**. The curriculum spans 36 months and emphasises algorithmic depth, mathematical rigour, data engineering, and production‑grade generative AI.

| Goal | Target |
| :--- | :--- |
| **Roles** | AI Engineer, LLM Engineer, MLOps Engineer |
| **Academic** | M.Sc. in AI / Data Science (Germany, 2028) |
| **Methodology** | 100% open‑source, reproducible environments, production documentation |

---

## 🛠️ Current Technology Stack
> *Actively updated as phases progress*

| Category | Tools |
| :--- | :--- |
| **Languages** | Python 3.12, C++ |
| **Core AI/ML** | NumPy, Matplotlib *(→ PyTorch / TensorFlow)* |
| **Infrastructure & Ops** | Linux (WSL2), uv package manager, Git/GitHub workflows |
| **Algorithms** | NeetCode 150 / LeetCode optimisation |

---

## 🗺️ Architectural Roadmap

| Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5+ |
| :---: | :---: | :---: | :---: | :---: |
| **Programming Foundations** | **Algorithm Engineering** | **Dev Env & AI Tools** | **Mathematics + German A2** | **Data Engineering → ML → LLM → MLOps** |
| ✅ Complete | 🔄 Active | 🔄 Active | ⏳ Upcoming | ⏳ Upcoming |

> 📘 **Detailed phase logs** are maintained in the [phases/](phases/) directory.

---

## 📚 Master Curriculum & Phase Audit Logs

### 🟢 Phase 01: Programming Foundations & Infrastructure (✅ Completed)
This sprint built the core execution environment and programming paradigms for high‑performance AI.
- **Environment Virtualisation:** Deterministic dependency resolution with uv (Python 3.12).
- **Architectural Paradigms:** OOP – multi‑class inheritance, encapsulated data structures.
- **Mathematical Computation:** Vectorised operations & memory‑efficient tensors via NumPy.
- **Data Serialisation:** Robust schema validation with Pydantic V2.
- **Version Control:** Daily Git workflow (branching, merge resolution, commit discipline).
- **Deliverable:** Unbroken daily commit record – all Phase 1 scripts integrated with uv environment.

### 🟡 Phase 02: Algorithm Engineering & Optimisation (🔄 Active Sprint)
Focus on space‑time complexity (Big O) and moving from brute‑force to optimised patterns.
- **Target:** 50 high‑quality solutions from the NeetCode 150 benchmark.
- **Core Topologies:** Arrays, hash maps, stacks, binary search trees, graph traversal.
- **Methodology:** Deep pattern recognition > passive repetition.
   *“50 analysed algorithms > 200 brute‑forced solutions.”*
- **Current Execution:** Complexity analysis documented natively in .py files.

### ⏳ Upcoming Phases (03 – 10)

| Phase | Focus |
| :---: | :--- |
| **03** | Dev Environment & AI Tools (Linux, Bash, SSH, Continue.dev) |
| **04** | Mathematics for AI (Linear Algebra, Calculus) + German A2 |
| **05** | Data Engineering (SQL, Pandas, pgvector, DVC, Prefect) |
| **06** | Classical ML (XGBoost, SHAP, Scikit‑Learn) |
| **07** | Production Engineering (FastAPI, Docker, CI/CD, evals gate) |
| **08** | Deep Learning (PyTorch, Karpathy series, Hugging Face) |
| **09** | MLOps, Responsible AI, Alignment (RLHF, LoRA), Feature Stores |
| **10** | Generative AI, Advanced RAG Evaluation, GraphRAG, Agents |

---

## 🇩🇪 German A2 Parallel Track (Mandatory)
From Phase 4 onward, 30 min/day of German is required.

| Resource | Link | Notes |
| :--- | :--- | :--- |
| **Learn German with Anja** | [youtube.com/@LearnGermanWithAnja](https://youtube.com/@LearnGermanWithAnja) | English explanations, slow, fun – start with A1 playlist |
| **Duolingo** | [duolingo.com](https://duolingo.com) | Gamified, builds basic vocab & grammar |
| **Goethe Institute** | [goethe.de/en/spr/ueb.html](https://www.goethe.de/en/spr/ueb.html) | Free, structured A1 exercises (sign‑up required) |
| **DW Learn German** | [learngerman.dw.com/en](https://learngerman.dw.com/en) | Try Nicos Weg A1 (if site is accessible) |

**Weekly routine:**
- Daily: 10 min Duolingo + 15 min YouTube lesson
- Weekly progress log in [language-log/](language-log/) (words learned, lessons completed)

---

## ✨ Portfolio & Shipped Deliverables

| Project | Phase | Stack | Link |
| :--- | :---: | :--- | :--- |
| **Neural Net (from scratch)** | 04 | NumPy MNIST classifier | [→ implementation](projects/neural-net-from-scratch/) |
| **SHAP ML Explainer** | 06 | XGBoost + SHAP values | [→ implementation](projects/shap-ml-demo/) |
| **Production RAG Chatbot** | 10 | LLM agents, vector DBs | [→ implementation](projects/rag-chatbot/) |

> *More projects will appear as phases complete.*

---

## 🚀 Reproduction & Local Setup
This repository uses [uv](https://astral.sh/uv) – a Rust‑based, fast Python package manager.

    # Clone the repository
    git clone https://github.com/AbdurrehmanAzam/production-llm-engineer-track.git
    cd production-llm-engineer-track

    # Sync the environment
    uv sync

    # Run a script
    uv run <script_name>.py

---

## 🤝 Contribution & License
This is a public learning track. You are welcome to:
- Adapt the roadmap
- Submit PRs for code optimisation
- Open issues for architectural discussions

📄 [Contribution Guidelines](CONTRIBUTING.md) · 📜 [MIT License](LICENSE)

<br/>
<div align="center">
  <i>“The best time to start was yesterday. The second best time is now.”</i><br/><br/>
  <b><a href="mailto:abdurrehmanazam300@gmail.com">✉️ Email</a></b> • <b><a href="https://github.com/AbdurrehmanAzam">🐙 GitHub Profile</a></b>
</div>
