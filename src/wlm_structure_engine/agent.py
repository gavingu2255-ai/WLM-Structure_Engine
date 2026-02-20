"""
WLM-Agent-Behavior — Structure → Stable, Interpretable Actions (MVP)
"""

from typing import Dict, Any


class Agent:
    """
    Minimal v0.1 Agent that takes a structural world state
    and produces a single action with a structural explanation.
    """

    def __init__(self, structure: Dict[str, Any]):
        self.structure = structure

    def next_action(self) -> Dict[str, Any]:
        """
        Generate a stable, interpretable action from structure.

        v0.1 logic:
        - if there is an injured entity (implied by tension + actors), approach and help
        - otherwise, explore or observe based on intent
        """
        actors = self.structure.get("actors", [])
        tension = self.structure.get("tension", "unknown")
        intent = self.structure.get("intent", "unknown")

        # Naive decision rules for v0.1
        if "wolf" in actors and tension in ("medium", "high"):
            return {
                "action_type": "approach",
                "target": "wolf",
                "reason": "Detected non-hostile tension + injured or vulnerable entity",
            }

        if intent == "exploration":
            return {
                "action_type": "explore",
                "target": self.structure.get("spatial", ["environment"])[0],
                "reason": "Intent is exploration; environment available",
            }

        return {
            "action_type": "observe",
            "target": "environment",
            "reason": "No strong intent or tension; default to observation",
        }
