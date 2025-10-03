from setuptools import setup, find_packages

setup(
    name="mlproject",
    version="0.2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    "click",
    "kagglehub"
],
    entry_points={
        "console_scripts": [
            "mlproject=mlproject.cli:cli",
        ],
    },
    author="Hitesh Pradhan",
    author_email="htshpradhan5@gmail.com",
    license="MIT License",
    description="MLProject CLI: Build quick and modular ML project scaffolding",
    url="https://github.com/pradhanhitesh/mlproject",
    python_requires=">=3.8",
)
