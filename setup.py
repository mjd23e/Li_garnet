from setuptools import setup, find_packages

setup(
    name='li_garnet',
    version='0.1.0',
    packages=find_packages(),
    description='Tools and utilities for lithium garnet projects',
    author='Mahesh Jagathpriya Dheerasinghe',
    author_email='md2023fsu@gmail.com',
    url='https://github.com/mjd23e/Li_garnet',
    python_requires=">=3.9",
    install_requires=[
        "pymatgen>=2024.0.0",
        "numpy>=1.23",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
