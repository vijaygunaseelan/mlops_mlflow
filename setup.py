import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "mlops_mlflow"
AUTHOR_USER_NAME = "vijaygunaseelan"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "vijaysiva2409@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/vijaygunaseelan/mlops_mlflow ",
    project_urls={
        "Bug Tracker": f"https://github.com/vijaygunaseelan/mlops_mlflow /issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)