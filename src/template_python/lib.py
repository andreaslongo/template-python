from pathlib import Path
import logging
import sys

log = logging.getLogger(__name__)


def run_app():
    log.error("Test log")
    print(say_hello())


def say_hello():
    return "Hi there."


def init_log(verbose: int = 0, logfile: Path | None = None) -> None:
    """Configures the logging system based on the verbosity level and optional
    logfile.

    Parameters:
    verbose (int): Verbosity level of logging.
                   0 - ERROR
                   1 - WARNING
                   2 - INFO
                   3 or higher - DEBUG
    logfile (Path, optional): Path to the logfile. If None, logs are
    only output to stderr.

    This function sets up the logging configuration with a specified verbosity
    level and an optional logfile.

    The log format includes the timestamp, log level, and logger name. The
    timestamp is formatted according to RFC3339.
    """
    match verbose:
        case 0:
            level = logging.ERROR
        case 1:
            level = logging.WARNING
        case 2:
            level = logging.INFO
        case _:
            level = logging.DEBUG

    format = "[%(asctime)s %(levelname)-8s %(name)s] %(message)s"
    RFC3339 = "%Y-%m-%dT%H:%M:%SZ"
    if logfile:
        handlers = [
            logging.FileHandler(logfile.resolve()),
            logging.StreamHandler(sys.stderr),
        ]
    else:
        handlers = [
            logging.StreamHandler(sys.stderr),
        ]

    logging.basicConfig(
        level=level,
        format=format,
        datefmt=RFC3339,
        handlers=handlers,
    )
