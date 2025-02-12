import logging
from template_python import cli

log = logging.getLogger(__name__)


def main():
    try:
        cli.run()
    except Exception as e:
        log.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
