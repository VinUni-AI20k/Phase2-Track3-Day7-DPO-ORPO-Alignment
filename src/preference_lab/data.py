from __future__ import annotations
import json
from pathlib import Path
from .schemas import PreferenceExample

def load_jsonl(path: str | Path) -> list[PreferenceExample]:
    """Load preference examples from JSONL.

    TODO(student): add line-numbered errors, duplicate prompt checks, and optional PII guardrails.
    """
    examples: list[PreferenceExample] = []
    with Path(path).open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            examples.append(PreferenceExample.model_validate(json.loads(line)))
    return examples

def split_by_prompt(examples: list[PreferenceExample], validation_ratio: float = 0.2) -> tuple[list[PreferenceExample], list[PreferenceExample]]:
    """Split examples by prompt to avoid leakage.

    TODO(student): implement deterministic shuffling by seed and grouping by prompt.
    Current skeleton returns a simple split for demonstration only.
    """
    cut = max(1, int(len(examples) * (1 - validation_ratio)))
    return examples[:cut], examples[cut:]
