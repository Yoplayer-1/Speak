import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Yoplayer_1", # Replace with your own username
    version="0.0.1",
    author="Tony",
    author_email="nairyashas@gmail.com",
    description="A small package for using the pyttsx3 module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yoplayer-1/Speak",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
