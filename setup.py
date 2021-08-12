"""Python setup.py for smarter package"""

from setuptools import find_packages, setup

setup(
    name="smarter",
    version="0.1.1",
    description="Some objects could be smarter",
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
