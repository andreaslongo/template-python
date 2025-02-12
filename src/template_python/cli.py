from pathlib import Path
import argparse
import logging
from template_python import lib


log = logging.getLogger(__name__)


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Increase verbosity level"
    )
    parser.add_argument(
        "--logfile",
        type=Path,
        help="Write log messages to a file (e.g., ./logfile.txt)",
    )
    args = parser.parse_args()
    lib.init_log(args.verbose, args.logfile)

    lib.run_app()
