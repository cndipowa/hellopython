from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
name='hellopython',
version='0.0.1',
description='Say Hello',
long_description=long_description,
long_description_content_type="text/markdown",
py_modules=["hellopython"],
package_dir={'':'src'},
install_requires = [
    "dnspython ~=2.0.0",
    "python-consul ~=1.1.0",    
],
extras_require = {
    "dev": [
        "pytest>=3.7",
    ],
},    
)
