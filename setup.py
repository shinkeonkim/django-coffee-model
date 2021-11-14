from setuptools import setup, find_packages

setup(
    name="django-coffee-model",
    version="0,1",
    description="django coffee models",
    author="shinkeonkim",
    author_email="singun11@kookmin.ac.kr",
    url="https://github.com/shinkeonkim/django-coffee-model",
    download_url="",
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=["django", "models"],
    python_requires=">=3",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
