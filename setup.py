"""setup.py"""
from os.path import dirname, join, abspath
from setuptools import setup, find_packages

__DESCRIPTION = """\
1secmail unofficial API, supporting random email generation, fetching messages and downloading attachments\
"""

__PROJECT_NAME = "onesecmail-api"

with open(
    join(abspath(dirname(__file__)), "README.md"),
    "r",
    encoding="utf-8",
    errors="ignore",
) as fp:
    __LONG_DESCRIPTION = fp.read().lstrip().rstrip()

setup(
    name=__PROJECT_NAME,
    version="0.1.1",
    author="st1vms",
    author_email="stefano.maria.salvatore@gmail.com",
    description=__DESCRIPTION,
    long_description=__LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/st1vms/onesecmail-api",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=["requests"],
)
