from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


def license():
    with open('LICENSE') as f:
        return f.read()


setup(
    name="funpdbe_validator",
    version="1.0.0",
    description="Validate PDBe-KB JSONs by FunPDBe Schema",
    long_description=readme(),
    classifiers=[
        "Development Status :: 3 - Beta",
        "License :: OSI Approved :: Apache 2 License",
        "Programming Language :: Python :: 3",
    ],
    keywords="json validator",
    url="https://github.com/PDBe-KB/funpdbe-validator",
    author="Mihaly Varadi",
    author_email="mvaradi@ebi.ac.uk",
    license=license(),
    packages=["validator"],
    install_requires=["jsonschema", "requests"],
    test_suite="tests",
    tests_require=["pytest", "pytest-cov"],
    include_package_data=True,
    zip_safe=True,
)

