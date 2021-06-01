from  setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name='break-time-kevon-scott',
    version='0.0.1',
    author='Kevon Scott',
    description='A python program for alerting user to take break',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows 10" 
    ],
    package_dir={"": "break_time"},
    packages=find_packages(where="break_time"),
    python_requires=">=3.6"
)