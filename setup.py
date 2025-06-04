from setuptools import setup, find_packages

setup(
    name="database_organizer",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add your dependencies here
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for organizing database files in a structured way",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
) 