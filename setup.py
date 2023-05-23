from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='nanorpc',
    version='0.0.2',
    packages=find_packages(),
    install_requires=['aiohttp', 'asyncio'],
    python_requires='>=3.7',
    author='gr0vity',
    url="https://github.com/gr0vity-dev/nanomock",
    description=
    'async nano rpc library with dynamic method generation per node version',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
