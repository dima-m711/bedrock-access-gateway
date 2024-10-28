


def add_token_usage_stats(model: str, input: int, output: int, cost: float ) -> None:
    """Add token usage stats to json file for tracking group by date and model.
    Args:
        model (str): Model name.
        input (int): Number of tokens used.
        output (int): Number of tokens generated.
        cost (float): Cost of tokens used.
    """
    from datetime import datetime
    from pathlib import Path
    from json import loads, dumps

    stats_file = Path("stats.json")
    if stats_file.exists():
        with stats_file.open("r") as f:
            stats = loads(f.read())
    else:
        stats = {}

    today = datetime.today().strftime("%Y-%m-%d")
    if today not in stats:
        stats[today] = {}

    if model not in stats[today]:
        stats[today][model] = {"input": 0, "output":0 , "cost": 0.0}

    stats[today][model]["input"] += input
    stats[today][model]["output"] += output
    stats[today][model]["cost"] += cost

    with stats_file.open("w") as f:
        f.write(dumps(stats, indent=4, sort_keys=True))

