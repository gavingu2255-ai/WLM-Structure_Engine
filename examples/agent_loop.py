"""
Minimal runnable example for WLM-Structure-Engine v0.1

Demonstrates:
- Input → Structure (SLP)
- Structure → Behavior (Agent)
"""

from wlm_structure_engine import parse, Agent
from wlm_structure_engine.utils import pretty_print


def main() -> None:
    text = "A traveler enters the forest and finds an injured wolf."

    print("Input:")
    print(text)
    print("\n---\n")

    structure = parse(text)
    print("Structure:")
    pretty_print(structure)
    print("\n---\n")

    agent = Agent(structure)
    action = agent.next_action()
    print("Agent Action:")
    pretty_print(action)


if __name__ == "__main__":
    main()
