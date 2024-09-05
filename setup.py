from setuptools import setup, find_packages

setup(
    name="satisfactory_toolbelt",
    version="0.1",
    description="Library with tools for Satisfactory game",
    author="Gustavo Miller",
    packages=find_packages(include=["docs_parser"]),
    install_requires=["pytest"],
)