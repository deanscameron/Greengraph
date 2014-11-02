""" Setup file for Greengraph"""

from setuptools import setup, find_packages

setup(
    name = "Greengraph",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greengraph.py'],
    install_requires = ['geopy', 'pypng', 'requests']
)