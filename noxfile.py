import nox  # type: ignore

nox.options.sessions = ["test", "lint"]


@nox.session(python=["3.8", "3.9", "3.10", "3.11", "3.12"])
def test(session):
    session.install(".[test]")
    session.run("pip", "check")
    session.run("pytest")


@nox.session
def lint(session):
    session.install(".[lint]")
    session.run("pip", "check")
    session.run("ruff", "check", ".")
    session.run("ruff", "format", "--diff", "--quiet", ".")


@nox.session
def dev(session):
    session.install("--editable", ".[test, lint]")
    session.run("pip", "check")
