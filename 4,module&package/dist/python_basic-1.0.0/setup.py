from setuptools import setup, find_packages

setup(
    name="python_basic",
    version="1.0.0",
    packages=find_packages(),  # 自動的にパッケージを見つける
    url="https://kaimu-seino.com",
    license="Free",
    author="kaimu",
    author_email="",
    description="Sample package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)