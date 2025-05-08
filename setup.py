from setuptools import setup

setup(
    name='openpylivox',
    version='1.1.1',
    url='https://github.com/zahidpichen/openpylivox',
    author='Zahid Pichen',
    author_email='zahidpichen1@gmail.com',
    packages=['openpylivox'],
    description='Python3 driver for Livox lidar sensors',    
    install_requires=['numpy >= 1.15.4', 'crcmod >= 1.7.0', 'deprecated >= 1.2.7', 'laspy >= 1.7.0', 'tqdm >= 4.48.0'],
    python_requires='>=3.5',
)
