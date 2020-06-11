import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="antiblock-scrapy",
    version="0.0.1",
    author="Elves M. Rodrigues",
    author_email="elvesmateusrodrigues@gmail.com",
    description="Mecanismos antibloqueios para Scrapy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elvesrodrigues/antiblock-scrapy",
    packages=setuptools.find_packages(),
    install_requires=[
        'pysocks==1.7.1',
        'requests==2.23.0',
        'stem==1.8.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.0',
)
