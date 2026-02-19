# WLM‑Agent‑Behavior  
**Dimensional structure → stable, interpretable actions**

The **WLM‑Agent‑Behavior** layer transforms structured semantics into **deterministic, interpretable actions**.  
It is the second core component of the WLM‑Structure‑Engine and the first layer that produces **behavior**.

This layer connects:

1. SLP structure  
2. Agent decision logic  
3. Persona traits  
4. Knowledge constraints  
5. World affordances  

The result is **stable, reproducible agent behavior**.

---

## ✨ Why this exists

Most agent systems today:

- hallucinate actions  
- behave inconsistently  
- lack causal grounding  
- cannot explain decisions  
- collapse under long‑term interaction  

WLM‑Agent‑Behavior fixes this by grounding actions in **explicit structure**.

It provides:

- deterministic action selection  
- interpretable reasoning  
- persona‑consistent behavior  
- tension‑aware decisions  
- causal justification  

This is **behavior as protocol**, not as sampling.

---

## ✨ Features

### **1. Structural Action Selection**
Actions are derived from dimensional fields:

- intent  
- tension  
- actors  
- objects  
- causal chains  
- environmental affordances  

### **2. Action Types (MVP)**

- approach  
- avoid  
- help  
- attack  
- negotiate  
- observe  
- explore  

### **3. Structured Reasoning**
Every action includes a causal explanation:

```json
{
  "action_type": "approach",
  "reason": "non-hostile tension + injured entity"
}
```

### **4. Persona Integration**
Behavior respects:

- traits  
- roles  
- motivations  
- invariants  

### **5. Deterministic Protocol**
Same structure → same action.

---

## 🧪 Example

Input structure:

```json
{
  "actors": ["traveler", "wolf"],
  "intent": "exploration",
  "tension": "medium",
  "objects": ["forest"]
}
```

Output:

```json
{
  "action_type": "approach",
  "target": "wolf",
  "reason": "Detected non-hostile tension + injured entity"
}
```

---

## 📦 API

### `Agent(structure).next_action() → dict`

```python
class Agent:
    def next_action(self) -> dict:
        """
        Generate a stable, interpretable action from structure.
        """
```

---

## 🧩 Summary

WLM‑Agent‑Behavior is the **first behavioral layer** of the WLM stack.  
It turns structure into **stable, interpretable, persona‑compatible actions**, enabling:

- consistent agents  
- causal decision‑making  
- transparent reasoning  
- world‑ready behavior  

A core component of the **WLM‑Structure‑Engine**.
