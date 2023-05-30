"""Commands to run in isolated venv."""
import nox
from nox import Session, session


@session(python="3.10")
def tests(session: Session) -> None:
    """Run all tests."""
    session.install(
        "coverage[toml]",
        "pytest",
        "pytest-cov",
    )
    args = session.posargs or ["tests", "--cov"]
    session.run("pip", "install", "-e", ".")
    session.run("pytest", *args)
