import setuptools

setuptools.setup(
    name="juxta",
    version="0.1.0",
    author="Rudy Williams",
    author_email="rudysw05@knights.ucf.edu",
    description="A package for flagging inconsistent records between two datasets",
    url="https://github.com/RudyWilliams/juxta",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["juxta=juxta.__main__:main"]},
    install_requires=["pandas", "openpyxl", "xlrd"],
)
