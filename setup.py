from setuptools import setup
# NOTE: necessary to import __version__

from os import path
with open(path.join(path.abspath(path.dirname(__file__)), "README.md")) as f:
    readme = f.read()

setup(
    name='lionplot',
    version="0.1.0",
    license='MIT',
    # url='TODO',
    author='Leonardo Alchieri',
    author_email='leonardo@alchieri.eu',
    description='Make lionplot',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=['scatterplot', 'lionplot', 'confidence interval'],
    packages=['lionplot'],
    # py_modules=['apple_heartrate_pandas'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
    install_requires=[
    'numpy',
    'seaborn',
    'matplotlib',
]
)