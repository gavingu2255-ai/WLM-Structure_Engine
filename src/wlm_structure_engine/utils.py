"""
Utility helpers for WLM-Structure-Engine (logging, pretty-printing, etc.)
"""

from typing import Any
import json


def pretty_print(obj: Any) -> None:
    """
    Pretty-print a Python object as JSON.
    """
    print(json.dumps(obj, indent=2, ensure_ascii=False))
