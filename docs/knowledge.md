# WLM‑Knowledge‑Engine  
**Dimensional structure → structured knowledge**

The **WLM‑Knowledge‑Engine** converts unstructured information into **explicit dimensional knowledge graphs**.  
It is the structural alternative to embedding‑based “token soup” and provides the semantic backbone for reasoning, memory, and world interaction.

This layer connects:

1. SLP structure  
2. Entity extraction  
3. Causal modeling  
4. Temporal ordering  
5. Knowledge graph construction  

It enables **interpretable, inference‑ready knowledge**.

---

## ✨ Why this exists

Traditional knowledge systems rely on:

- embeddings  
- vector similarity  
- opaque memory stores  
- non‑causal associations  

These approaches cannot guarantee:

- interpretability  
- causal reasoning  
- temporal consistency  
- stable retrieval  

The WLM‑Knowledge‑Engine fixes this by grounding knowledge in **dimensional structure**.

It produces:

- structured facts  
- causal chains  
- temporal sequences  
- hierarchical categories  
- inference‑ready graphs  

This is **knowledge as protocol**, not as vectors.

---

## ✨ Features

### **1. Structured Fact Extraction**
Converts text into explicit knowledge units.

### **2. Causal Graph Construction**
Builds cause‑effect relationships.

### **3. Temporal Ordering**
Places events on a timeline.

### **4. Entity & Relation Modeling**
Defines:

- entities  
- attributes  
- relations  
- roles  

### **5. Inference Hooks**
Knowledge can be used by:

- agents  
- personas  
- world models  
- metacognition  

---

## 🧪 Example

Input:

```
Wolves avoid fire because it threatens their survival.
```

Output:

```json
{
  "entity": "wolf",
  "relation": "avoids",
  "object": "fire",
  "cause": "threatens survival",
  "category": "behavioral rule"
}
```

---

## 📦 API

### `extract_knowledge(structure: dict) → dict`

```python
def extract_knowledge(structure: dict) -> dict:
    """
    Convert structured input into a knowledge unit.
    """
```

---

## 🧩 Summary

The WLM‑Knowledge‑Engine turns structure into **interpretable, causal, temporal knowledge**.  
It enables:

- structured reasoning  
- stable memory  
- causal inference  
- world‑model grounding  

A key component of the WLM structural cognition pipeline.
