from setuptools import setup, find_packages

from willhaben import __version__

setup(
    name='Willhaben',
    version=__version__,

    url='https://github.com/CP02A/willhaben-python',
    author='Christian Proschek',
    author_email='christian@proschek.dev',

    py_modules=find_packages(),
)