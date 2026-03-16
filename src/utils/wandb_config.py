import wandb
from datetime import datetime
from pathlib import Path

ROOT = Path.cwd().parents[2]
link_file = ROOT / "wandb_link.txt"

PROJECT_NAME = "credit-card-fraud-detection"

def start_run(model_name, config=None):

    run = wandb.init(
        project=PROJECT_NAME,
        name=model_name,
        config=config
    )

    date = datetime.now().strftime("%Y-%m-%d")

    with open(link_file, "a", encoding="utf-8") as f:
        f.write(f"\nModel: {model_name}\n")
        f.write(f"Date: {date}\n")
        f.write(f"Run URL: {run.url}\n")

    return run


def log_metrics(metrics: dict):
    wandb.log(metrics)


def finish_run():
    wandb.finish()
