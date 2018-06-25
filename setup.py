import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deck_of_cards",
    version="0.0.9",
    author="Simon Lachaîne",
    author_email="simonthechain@gmail.com",
    description="A module to create and interact with a deck of cards object",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SimonTheChain/deck_of_cards",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
