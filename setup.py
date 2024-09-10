from setuptools import setup, find_packages

setup(
    name='xtractr',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    description='A modular web scraping framework.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/xtractr',
)