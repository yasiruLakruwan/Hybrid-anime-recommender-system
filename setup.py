from setuptools import setup,find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Hybrid-anime-recommendor',
    version='0.0.1',
    author='yasiru',
    packages=find_packages(),
    install_requires= requirements
)