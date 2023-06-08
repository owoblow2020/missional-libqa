"""
Setup library website
"""

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="library",
    version="0.0.0",
    description="Missional University Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://teamwork.missional.university/university/software-development/libaq",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
    package_dir={"": "library"},
    packages=find_packages(where="library"),
    python_requires=">=3.6, <4",
    install_requires=[
        "Django==3.2.8",
        "django-cors-headers==3.10.0",
        "djangorestframework==3.12.4",
        "mozilla-django-oidc==2.0.0",
        "psycopg2==2.9.1",
    ],
    extras_require={
        "dev": [
            "pylint==2.11.1",
            "black==21.9b0",
        ],
        "test": [
            "pytest==6.2.5",
            "pytest-cov==3.0.0",
        ],
    },
    project_urls={
        "Bug Reports": (
            "https://teamwork.missional.university/university/software-development/libaq/-/issues"
        ),
        "Source": "https://teamwork.missional.university/university/software-development/libaq",
    },
)
