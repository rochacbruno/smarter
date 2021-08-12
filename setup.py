"""Python setup.py for smarter package"""
from pathlib import Path
from setuptools import find_packages, setup

setup(
    name="smarter",
    version="0.1.4",
    description="Some objects could be smarter",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Bruno Rocha",
    packages=find_packages(exclude=["tests"]),
    install_requires=[],
    extras_require={
        "test": [
            "pytest",
            "coverage",
            "flake8",
            "black",
            "isort",
            "pytest-cov",
            "codecov",
            "mypy",
            "gitchangelog",
        ],
    },
)
