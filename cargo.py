#!/usr/bin/env python3

def main():
    import argparse
    import subprocess

    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", title="commands")
    commands.add_parser("clippy", help="Checks a package to catch common mistakes and improve your Python code.")
    commands.add_parser("dev", help="Initialize a local DEV environment.")
    commands.add_parser("fmt", help="Formats all Python files of the local package using black.")
    commands.add_parser("nox", help="Execute all nox sessions.")
    commands.add_parser("test", help="Execute all unit and integration tests and build examples of a local package")
    args = parser.parse_args()

    if args.command == "clippy": subprocess.run((".nox/dev/bin/ruff", "check", "."))
    if args.command == "dev": subprocess.run(("python3", "-m", "pipx", "run", "nox", "--session", "dev"))
    if args.command == "fmt": subprocess.run((".nox/dev/bin/black", "--quiet", "--preview", "."))
    if args.command == "nox": subprocess.run(("python3", "-m", "pipx", "run", "nox"))
    if args.command == "test": subprocess.run((".nox/dev/bin/pytest"))

if __name__ == "__main__":
    main()
