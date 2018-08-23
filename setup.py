# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license0 = f.read()

setup(
    name='pycnic',
    version='0.0.1',
    description='Automated quiz for mri images',
    long_description=readme,
    author='Odelin Charron, Vincent Noblet',
    author_email='audy322@hotmail.fr',
    url='https://github.com/OdelinCharron/pycnic',
    license=license0,
    packages=find_packages(exclude=('tests', 'docs', 'examples')),
    scripts=['pycNic']
)
