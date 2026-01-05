# AI Agent Framework

## Overview
This project implements a custom **AI Agent Framework** that executes AI agents as **workflow-based task flows** using a reusable orchestrator.

Agents are defined using JSON workflows and executed with retry logic, state management, metrics, and observability.

---

## Architecture
Ingress → Orchestrator → Executors → State & Memory → Output

- Orchestrator inspired by Apache Airflow
- Executors are pluggable (LLM, OCR, Tools)
- State store simulates Redis/PostgreSQL
- Flask provides a lightweight visualization layer

---

## Reference Agents
1. **Document Analysis Agent**
   - OCR → LLM Summary

2. **Customer Support Agent**
   - Query Normalization → LLM Response

---

## How to Run (Terminal)
```bash
cd ai_agent_framework
python main.py
