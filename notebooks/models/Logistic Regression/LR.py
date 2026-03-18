import wandb
import random

wandb.login()

run = wandb.init(
    entity="khoaa6k5-ou",  # 👈 dùng TEAM, không dùng username nữa
    project="credit-card-fraud",
    name="logistic-regression",
    config={
        "learning_rate": 0.02,
        "architecture": "Logistic Regression",
        "dataset": "Credit Card Fraud",
        "epochs": 10,
    },
)

epochs = 10
offset = random.random() / 5

for epoch in range(2, epochs):
    acc = 1 - 2**-epoch - random.random() / epoch - offset
    loss = 2**-epoch + random.random() / epoch + offset

    run.log({
        "epoch": epoch,
        "accuracy": acc,
        "loss": loss
    })

run.finish()