import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# Version of the project
__version__ = "0.0.1"

REPO_NAME = "Kidney-Disease-Classification-Deep-Learning-Project"
AUTHOR_USER_NAME = "Naman-1934"
SRC_REPO = "KidneyDiseaseClassification"
AUTHOR_EMAIL = "naman532002@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A Small python package for CNN app",
    long_description = long_description,
    long_descripion_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")

)