from setuptools import setup, find_packages

setup(
    name="numero_espanol",
    version="0.1.0",
    packages=find_packages(),
    description="Biblioteca para convertir números escritos en español a valores numéricos",
    author="Tu Nombre",
    author_email="tu@email.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)