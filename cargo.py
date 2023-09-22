#!/usr/bin/env python3


def main():
    import argparse
    import subprocess
    from pathlib import Path
    import sys
    import shutil

    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", title="commands")
    commands.add_parser("build", help="Builds the package.",)
    commands.add_parser("clippy", help="Checks a package to catch common mistakes and improve your Python code.",)
    commands.add_parser("dev", help="Initialize a local DEV environment.")
    commands.add_parser("fmt", help="Formats all Python files of the local package using black.")
    commands.add_parser("nox", help="Execute all nox sessions.")
    commands.add_parser("test", help="Execute all unit and integration tests and build examples of a local package",)
    commands.add_parser("new", help="Create a new Python package").add_argument('path', type=Path)

    commands.add_parser("run", aliases=['r'], help="Run a module of the local package")

    args = parser.parse_args()

    if args.command == "build":
        subprocess.run(("python3", "-m", "pipx", "run", "build"))
    if args.command == "clippy":
        subprocess.run((".nox/dev/bin/ruff", "check", "."))
    if args.command == "dev":
        subprocess.run(("python3", "-m", "pipx", "run", "nox", "--session", "dev"))
    if args.command == "fmt":
        subprocess.run((".nox/dev/bin/black", "--quiet", "."))
    if args.command == "nox":
        subprocess.run(("python3", "-m", "pipx", "run", "nox"))
    if args.command == "test":
        subprocess.run((".nox/dev/bin/pytest"))
    if args.command == "new":
        if args.path.exists():
            print(f"error: path exists '{args.path.resolve()}'")
            sys.exit(1)
        shutil.copytree(
            src=Path('~/code/templates-python').expanduser().resolve(),
            dst=args.path,
            ignore=shutil.ignore_patterns('Session.*', '.git', '*.swp', 'cargo.py'),
            dirs_exist_ok=False,
        )
    if args.command in ["run", "r"]:
        p = Path(".nox/dev/")
        first_main = next(Path("src/").glob("**/__main__.py"))
        if not p.exists():
            subprocess.run(("python3", "-m", "pipx", "run", "nox", "--session", "dev"))
        subprocess.run((".nox/dev/bin/python3", first_main))


if __name__ == "__main__":
    main()
