from setuptools import setup, find_packages

setup(
    name="mlproject",
    version="0.1.5",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "numpy",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "mlproject=mlproject.cli:cli",
        ],
    },
    author="Your Name",
    description="ML project scaffolding CLI",
    url="https://github.com/pradhanhitesh/mlproject",
    python_requires=">=3.8",
)
