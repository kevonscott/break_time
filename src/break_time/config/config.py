from pathlib import Path

import yaml

with open((Path(__file__).parent / "config.yml"), "r") as yaml_file:
    cfg = yaml.safe_load(yaml_file)

REP_BASED_ACTIVITIES = cfg["REP_BASED_ACTIVITIES"]
TIME_BASED_ACTIVITIES = cfg["TIME_BASED_ACTIVITIES"]
ACTIVITIES = {
    "REP_BASED_ACTIVITIES": [REP_BASED_ACTIVITIES, "rep"],
    "TIME_BASED_ACTIVITIES": [TIME_BASED_ACTIVITIES, "minutes"],
}
REP_COUNT = [5, 10, 15]  # number of reps
