# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='charbeat',
    version='0.1',
    description='A charbeat/newsbeat API wrapper.',
    author='Timothée Peignier',
    author_email='timothee.peignier@tryphon.org',
    url='https://github.com/cyberdelia/chartbeat',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
