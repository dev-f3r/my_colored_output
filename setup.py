import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="colored output",
    version="0.0.1",
    description="python library to color console messages",
    long_description=README,
    long_description_content_type="text/markdown",
    url="", # TODO: add gh url.
    author="devf3r",
    author_email="devfercastro@gmail.com",
    license="MIT",
    # TODO: Add entry points if necessary.
    python_requires=">=3.11",
    # TODO: Add classifiers if necessary.
    packages=["colored_output"],
    # TODO: Add include_package_data if necessary.
    # TODO: Add install_requires if necessary.
)