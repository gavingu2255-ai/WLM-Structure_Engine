# WLM‑SLP — Structural Language Protocol  
**Language → Dimensional Structure**

The **Structural Language Protocol (SLP)** is the first layer of the WLM ecosystem.  
It transforms raw language into **explicit dimensional structure**, providing a stable semantic substrate for all higher‑level reasoning, behavior, and world interaction.

SLP is the foundation of the WLM‑Structure‑Engine:

1. Raw input  
2. Structural parsing  
3. Dimensional representation  
4. Behavior, persona, knowledge, and world hooks  

It replaces token‑level heuristics with deterministic structure:

> **Same input → same structure**

---

## ✨ Why SLP exists

Traditional NLP systems rely on:

- embeddings  
- heuristics  
- statistical co‑occurrence  
- opaque internal states  

These approaches cannot guarantee:

- consistency  
- interpretability  
- causal reasoning  
- stable agent behavior  

SLP solves this by grounding language in **dimensional semantics**.

It produces:

- interpretable structures  
- causal chains  
- actor‑intent mappings  
- tension and relational dynamics  
- spatial/temporal anchors  

This is **language as protocol**, not as prediction.

---

## ✨ Features

### **1. Actor Extraction**
Identifies all entities participating in the scene.

### **2. Intent Modeling**
Determines the driving force behind actions.

### **3. Object & Environment Parsing**
Extracts items, locations, and contextual elements.

### **4. Tension & Relational Dynamics**
Captures conflict, cooperation, uncertainty, and pressure.

### **5. Causal Structure**
Builds explicit cause‑effect chains.

### **6. Dimensional Anchors**
Adds spatial and temporal grounding.

---

## 🧪 Example

Input:

```
A traveler enters the forest and finds an injured wolf.
```

Output (MVP):

```json
{
  "actors": ["traveler", "wolf"],
  "intent": "exploration",
  "objects": ["forest"],
  "tension": "medium",
  "causal": ["traveler explores → encounters wolf"],
  "spatial": ["forest"],
  "temporal": ["present"]
}
```

---

## 📦 API

### `parse(text: str) → dict`

```python
def parse(text: str) -> dict:
    """
    Convert natural language into dimensional structure.
    """
```

---

## 🧩 Summary

SLP is the **entry point** of the WLM structural stack.  
It turns language into **interpretable, deterministic structure**, enabling:

- stable agent behavior  
- consistent personas  
- structured knowledge  
- transparent reasoning  
- world‑model integration  

A foundational component of the **WLM‑Structure‑Engine**.
