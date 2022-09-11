from invoke import Exit, UnexpectedExit, task

from . import common


@task
def isort(context, path=".", params=""):
    """Run isort."""
    context.run(f"isort {path} {params}")


@task
def flake8(context, path=".", params=""):
    """Run flake8 linter."""
    context.run(f"flake8 {path} {params}")


@task
def black(context, path=".", params=""):
    """Run black linter."""
    default_params = "--check --exclude='migrations/|.ipython/'"
    context.run(f"black {path} {params} {default_params}")


@task
def all(context, path="smcp"):
    """Run all linters."""
    linters = (isort, flake8, black)
    failed = []

    common.warn("Running linters")

    for linter in linters:
        try:
            common.information(linter.__name__)
            linter(context, path=path)
        except UnexpectedExit:
            failed.append(linter.__name__)

    if failed:
        common.error(f"Failed: {', '.join(failed)}")
        raise Exit(code=1)

    common.success("All checks passed")
