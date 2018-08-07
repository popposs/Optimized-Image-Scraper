import os

from setuptools import setup, find_packages

project_root = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(project_root, 'README.md')).read()
VERSION = open(os.path.join(project_root, 'VERSION')).read()

requires = [
    'praw'
]

setup(
    name='dashboard_lol',
    version=VERSION,
    description="Reddit Cat Scraper",
    long_description=README,
    classifiers=[
        "Programming Language :: Python"
    ],
    author='',
    author_email='',
    url='',
    keywords='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
