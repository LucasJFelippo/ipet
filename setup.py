from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="I-Pet",
    version="1.0.0",
    description="A simple university project.",
    author="Lucas Nunes de Felippe",
    author_email="LucasJFelippo@gmail.com",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    python_requires=">=3.8, <4",
    project_urls={
        "Figma": "",
    },
)