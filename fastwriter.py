from time import perf_counter
import requests
import random
from json import loads

from fastwrite.config import FastWriteConfig, read_config
from fastwrite.log import logger
from fastwrite.utils import change_dir

def main() -> None:
    """Main function."""
    logger.info("Starting up fastwriter...")
    start = perf_counter()
    config = read_config("./config.json")
    unpack_input_txt(config)
    logger.info("Getting response object...")

    output = write(config, True)

    with change_dir(config.export_dir):
        logger.info("Export directory: %s" % config.export_dir)
        filename = f'fastwritefile_{random.randint(1,100)}.txt'
        with open(filename,'w',encoding='utf-8') as f:
            f.write(output)
            logger.info("Filename: %s" % filename)
    elapsed = perf_counter() - start
    logger.info("Extraction finished in %s seconds. " % elapsed)

def write(config: FastWriteConfig, recursion: bool = False) -> str:
    output = ""

    for i in range(config.iterations):
        response = requests.post(
        url=config.url, json=config.payload, headers=config.headers
        )
        logger.info("Formatting response, number: %s" % i)
        doc: dict[str,str] = loads(response.text)[0]
        sample: str = doc.get("generated_text")
        output += sample
        if recursion == True:
            config.payload['context'] = sample
        continue

    return output

def unpack_input_txt(config: FastWriteConfig) -> None:
    with open(config.input_txt, encoding="utf8") as iowrapper:
        textlines: str = iowrapper.readline()
        config.payload['context'] = textlines

if __name__ == "__main__":
    main()
