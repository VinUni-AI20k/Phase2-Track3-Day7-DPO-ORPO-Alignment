from __future__ import annotations
from pathlib import Path
import typer
from rich import print
from .config import load_config
from .data import load_jsonl
from .evaluate import pairwise_accuracy, write_metrics

app = typer.Typer(help="Preference alignment lab CLI")

@app.command()
def validate(data: Path) -> None:
    examples = load_jsonl(data)
    print(f"[green]Loaded {len(examples)} preference examples[/green]")

@app.command()
def evaluate(config: Path) -> None:
    cfg = load_config(config)
    examples = load_jsonl(cfg["paths"]["train_data"])
    # TODO(student): replace mock scores with model logprob-based scores.
    chosen_scores = [1.0 for _ in examples]
    rejected_scores = [0.0 for _ in examples]
    metrics = {"pairwise_accuracy": pairwise_accuracy(examples, chosen_scores, rejected_scores)}
    out = write_metrics(metrics, cfg["paths"]["output_dir"])
    print(f"[green]Wrote metrics to {out}[/green]")

if __name__ == "__main__":
    app()
