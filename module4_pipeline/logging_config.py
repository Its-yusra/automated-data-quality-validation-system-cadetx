
import logging
from pathlib import Path


def setup_logging(output_dir, level="INFO"):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    log_file = output_dir / "pipeline.log"

    logger = logging.getLogger("data_pipeline")
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    logger.handlers.clear()
    logger.propagate = False

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        log_file, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
