import nox

nox.options.stop_on_first_error = False
lint_dependencies = ["mypy"]
format_dependencies = ["black", "isort"]


@nox.session(python=["3.6", "3.7", "3.8"])
def lint(session):
    """Lint the python file."""
    session.install(*lint_dependencies)
    session.install("-r", "requirements.txt")
    session.run("mypy", "test_file.py")


@nox.session(name="format", python=["3.6", "3.7", "3.8"])
def check_format(session):
    """Format the code and output the result."""
    session.install(*format_dependencies)
    session.run("black", "-l", "79", "--check", "--diff", "test_file.py")
