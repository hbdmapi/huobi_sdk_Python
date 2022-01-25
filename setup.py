import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="huobipy",
    version="1.0.1",
    author="adlong",
    author_email="3140618@163.com",
    description="huobi api sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hbdmapi/huobi_sdk_Python",
    project_urls={
        "Bug Tracker": "https://github.com/hbdmapi/huobi_sdk_Python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)