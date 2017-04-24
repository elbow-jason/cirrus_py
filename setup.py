"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open("requirements.txt", "r") as file_h:
    reqs = [l.strip() for l in file_h.readlines()]

setup(
    name='cirrus_py',
    version='0.1.0',
    description="Use Google Service Account JSON OAuth2 utility",
    long_description=long_description,
    url='https://github.com/elbow-jason/cirrus_py',
    author='Jason Goldberger',
    author_email='jlgoldb2@asu.edu',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='oauth oauth2 google-cloud',
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=reqs,
)
