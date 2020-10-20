"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name='facebook_tools',
    version='0.0.1',
    description='Tool for heling while developing for facebook',   
    url='https://github.com/osmay88/facebook-tools',   
    author='Osmay Cruz<osmay.cruz@gmail.com>',   
    author_email='osmay.cruz@gmail.com',   

    classifiers=[ 
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='python, facebook, facebook-cli',   
    package_dir={'': 'src'},   
    packages=find_packages(where='src'),
    python_requires='>=3.5, <4',
    project_urls={   
        'Bug Reports': 'https://github.com/osmay88/facebook-tools',
        # 'Funding': 'https://donate.pypi.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        # 'Source': 'https://github.com/pypa/sampleproject/',
    },
)