"""
WLM-SLP — Structural Language Protocol (MVP)

Language → Dimensional Structure
"""

from typing import Dict


def parse(text: str) -> Dict:
    """
    Convert natural language into a minimal dimensional structure.

    This is a v0.1 MVP implementation:
    - rule-based / placeholder logic
    - deterministic
    - designed to be replaced by richer structural parsing later
    """
    # Very naive placeholder logic for v0.1
    # In real versions, this would be replaced by a proper structural parser.
    structure = {
        "raw": text,
        "actors": [],
        "intent": "unknown",
        "objects": [],
        "tension": "unknown",
        "causal": [],
        "spatial": [],
        "temporal": ["present"],
    }

    lower = text.lower()

    # Extremely naive heuristics just to make the example "feel alive"
    if "traveler" in lower:
        structure["actors"].append("traveler")
    if "wolf" in lower:
        structure["actors"].append("wolf")
    if "forest" in lower:
        structure["objects"].append("forest")
        structure["spatial"].append("forest")

    if "enters" in lower or "explore" in lower or "exploration" in lower:
        structure["intent"] = "exploration"

    if "injured" in lower:
        structure["tension"] = "medium"
        structure["causal"].append("encounter injured entity")
    else:
        structure["tension"] = "low"

    return structure
