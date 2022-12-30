import inspect
import sys
from functools import partial

from invoke import task
from invoke.exceptions import UnexpectedExit

if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec


@task
def install_hooks(c):
    c.run("pre-commit install --install-hooks -t pre-commit -t pre-push ")


@task
def run_pylint(c):
    c.run("pylint --rcfile=.pylintrc receipt_reader tests")


@task
def run_isort(c, check=False):
    c.run(f"isort .{' --check' if check else ''}")


@task
def run_black(c, check=False):
    c.run(f"black .{' --check' if check else ''}")


@task
def format(c):
    run_isort(c, check=False)
    run_black(c, check=False)


@task
def lint(c):
    commands = (
        partial(run_isort, check=True),
        partial(run_black, check=True),
    )
    exit_code = 0
    for cmd in commands:
        try:
            cmd(c)
        except UnexpectedExit as err:
            exit_code = err.result.return_code
    if exit_code:
        sys.exit(exit_code)


@task
def test(c):
    c.run("pytest tests/")
