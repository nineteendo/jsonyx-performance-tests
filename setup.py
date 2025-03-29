"""jsonc setup."""
from __future__ import annotations

__all__: list[str] = []

# pylint: disable=import-error
from setuptools import Extension, setup  # type: ignore

if __name__ == "__main__":
    setup(
        name="jsonc",
        version="0.1.0",
        packages=["jsonc"],
        ext_modules=[Extension("_jsonc", ["src/jsonc/_speedups.c"])],
        package_dir={"": "src"},
    )
