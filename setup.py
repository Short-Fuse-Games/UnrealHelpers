from setuptools import setup, find_packages

setup(
    name="unreal_helpers",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        'coverage>=7.0.0',
    ],
    extras_require={
        'dev': [
            'coverage>=7.0.0',
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
        ],
    },
    python_requires='>=3.7',
) 