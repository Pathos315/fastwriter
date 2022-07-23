r"""config contains the dataclass describing
    the overall configurations
    and a method to read the config

    Returns:
        a function that reads the dataclass as a JSON object.
    """

import json
from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class FastWriteConfig:
    """A dataclass containing the overall configurations"""

    prog: str
    description: str
    log_dir: str
    export_dir: str
    input_txt: str
    url: str
    iterations: int
    payload: dict = field(default_factory=dict)
    headers: dict = field(default_factory=dict)

def read_config(config_file: str) -> FastWriteConfig:
    """read_config takes a .json file and returns a ScrapeConfig object.

    Args:
        config_file (str): the path to the .json file containing the configs.

    Returns:
        ScrapeConfig: A dataclass containing the overall configurations
    """
    with open(config_file, encoding="utf-8") as file:
        data = json.load(file)
        return FastWriteConfig(**data)
