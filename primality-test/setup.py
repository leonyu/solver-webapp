import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Primality Test",
    version="0.0.1",
    author="Leon Yu",
    author_email="leon@leonyu.net",
    description=("Farmat Primality Test"),
    packages=['primality', 'tests'],
)
