from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="imageprocessbcamp",
    version="0.0.1",
    author="brenobcamp",
    author_email="brenobatistacampos@gmail.com",
    description="Package for image processing",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/brenobcamp/image-processing.git",
    packages=find_packages(),
    python_requires='>=3.8',
)