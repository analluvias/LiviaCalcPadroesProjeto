from setuptools import setup, find_packages

setup(
    name="LiviaCalc",
    version="0.1",
    packages=find_packages(),
    description="Uma biblioteca de calculadora simples",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Seu Nome",
    author_email="seuemail@example.com",
    url="https://github.com/analluvias/LiviaCalcPadroesProjeto",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
