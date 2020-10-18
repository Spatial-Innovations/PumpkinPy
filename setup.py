import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pumpkinpy",
    version="0.1.1",
    author="Spatial Innovations",
    author_email="spatialinnovations@gmail.com",
    description="A Python module with utilities for many fields.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Spatial-Innovations/PumpkinPy",
    py_modules=["pumpkinpy"],
    packages=setuptools.find_packages(),
    install_requires=[
        "pygame ~= 1.9.6",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
) 
