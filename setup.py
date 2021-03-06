from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.2",
    author="agoyal-84",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agoyal-84/DVC-AIML-OPS",
    author_email="amitgoyalniitdeo@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc==2.7.3',
        'pandas',
        'scikit-learn'
    ]
)