import logging
from template_python.cli import run

log = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.ERROR)

    try:
        run()
    except Exception as e:
        log.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
