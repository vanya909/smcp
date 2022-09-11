from invoke import Collection

from provision import linters

ns = Collection(
    linters,
)
