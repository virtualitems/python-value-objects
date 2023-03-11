"""
Release configuration
"""

from pathlib import Path
from setuptools import setup


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


VERSION = '1.0.0'
DESCRIPTION = 'Python value object implementation'
PACKAGE_NAME = 'python-value-object'
AUTHOR = 'github@virtualitems'
EMAIL = 'virtualitemsuniverse@gmail.com'
GITHUB_URL = 'https://github.com/virtualitems'
LICENSE = 'MIT'


setup(
    name=PACKAGE_NAME,
    packages=['package'],
    version=VERSION,
    license=LICENSE,
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=GITHUB_URL,
    keywords=['value', 'object'],
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
)
