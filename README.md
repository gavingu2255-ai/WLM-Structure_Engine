# WLM‑Structure‑Engine  
**Dimensional structure → interpretable inputs, stable agents, structured cognition**

The **WLM‑Structure‑Engine** is the foundational execution layer of the WLM ecosystem.  
It transforms raw inputs into **dimensional structure**, enabling AI systems to act, reason, and interpret the world through explicit structural semantics rather than token‑level prediction.

This is the **core engine** behind the entire WLM stack:

1. WLM‑SLP‑Interpreter — Language → Structure  
2. WLM‑World‑Model‑Interpreter — World Model → Structure  
3. WLM‑Agent‑Behavior — Structure → Behavior  
4. WLM‑Persona‑Engine — Structure → Identity  
5. WLM‑Knowledge‑Engine — Structure → Knowledge  
6. WLM‑Metacognition‑Engine — Structure → Self‑Monitoring  
7. WLM‑World‑Generation‑Protocol — Structure → Worlds  

The WLM‑Structure‑Engine implements the **minimum runnable core** of this system:

> **Input → Structure → Behavior**

---

## ✨ Why this exists

Modern AI systems operate on:

- opaque embeddings  
- unstable reasoning paths  
- inconsistent agent behavior  
- non‑structural world representations  
- token‑level heuristics instead of dimensional semantics  

The WLM‑Structure‑Engine fixes this by grounding AI in **explicit structure**.

It provides:

- interpretable semantic structure  
- stable agent behavior  
- consistent persona logic  
- structured knowledge representations  
- transparent reasoning paths  
- deterministic world interactions  

This is **AI as a protocol**, not as a prompt.

---

## ✨ Features

### **1. Structural Language Protocol (SLP)**
Transforms any input (text, events, actions) into dimensional structure:

- actors  
- intents  
- objects  
- tensions  
- causal relations  
- spatial/temporal anchors  

### **2. Agent Behavior Engine**
Generates stable, reproducible, interpretable actions:

- approach / avoid / help / attack  
- negotiate / explore / observe  
- structured reasoning for each action  

### **3. Persona Structure Layer**
Defines identity through structure:

- traits  
- roles  
- motivations  
- behavioral invariants  

### **4. Knowledge Structuring**
Converts token soup into:

- structured facts  
- causal graphs  
- inference‑ready knowledge  

### **5. Metacognitive Monitoring**
Tracks:

- reasoning paths  
- structural consistency  
- dimension switching  
- self‑correction signals  

### **6. Protocol‑First Design**
Same structure → same behavior.  
Deterministic, interpretable, controllable.

---

## 🚀 Quickstart

### **Install**

```bash
pip install wlm-structure-engine
```

### **Use**

```python
from wlm_structure_engine import parse, Agent

text = "A traveler enters the forest and finds an injured wolf."

structure = parse(text)
agent = Agent(structure)
action = agent.next_action()

print("Structure:", structure)
print("Action:", action)
```

### **Output (MVP)**

```
Structure: {
  "actors": ["traveler", "wolf"],
  "intent": "exploration",
  "tension": "medium",
  "objects": ["forest"]
}

Action: {
  "action_type": "approach",
  "target": "wolf",
  "reason": "Detected non-hostile tension + injured entity"
}
```

---

## 🧠 How it works

The engine performs three core steps:

### **1. Input → Structural Representation**
SLP converts raw language into dimensional structure.

### **2. Structure → Behavioral Interpretation**
The Agent engine interprets structure to produce stable actions.

### **3. Structure → Cognitive Hooks**
Persona, knowledge, and metacognition layers attach to the same structure.

This forms the **minimum runnable loop** of WLM.

---

## 📦 API

### `parse(text: str) → dict`

```python
def parse(text: str) -> dict:
    """
    Convert natural language into dimensional structure.
    """
```

### `Agent(structure).next_action() → dict`

```python
class Agent:
    def next_action(self) -> dict:
        """
        Generate a stable, interpretable action from structure.
        """
```

---

## 🏗 Repository Structure

```
wlm-structure-engine/
│
├── LICENSE
├── README.md
├── pyproject.toml
├── setup.cfg
│
├── src/
│   └── wlm_structure_engine/
│       ├── __init__.py
│       ├── slp.py
│       ├── agent.py
│       ├── persona.py
│       ├── knowledge.py
│       ├── metacog.py
│       └── utils.py
│
├── examples/
│   └── agent_loop.py
│
└── docs/
    ├── overview.md
    ├── slp.md
    ├── agents.md
    ├── knowledge.md
    └── roadmap.md

```

---

## 📄 License

MIT License  
Copyright (c) 2026  
**Wujie Gu**

---

## 🧩 Summary

The **WLM‑Structure‑Engine** is the structural core of the WLM ecosystem.  
It turns raw input into **dimensional structure**, and structure into **stable, interpretable behavior**.

It enables:

- structural semantics  
- stable agents  
- consistent personas  
- structured knowledge  
- transparent reasoning  
- deterministic world interaction  

A foundational component of the **WLM generative stack**.
