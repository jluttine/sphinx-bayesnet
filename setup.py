# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys

long_desc = '''
This package contains BayesNet extension for Sphinx making it
easy to draw Bayesian networks, graphical models and (directed) factor
graphs in Sphinx. The extension is based on a TikZ library called
BayesNet.
'''

requires = ['Sphinx>=0.6',
            'sphinxcontrib-tikz>=0.4']

setup(
    name='sphinxcontrib-bayesnet',
    version='0.4',
    url='https://github.com/jluttine/sphinx-bayesnet',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-bayesnet',
    author='Jaakko Luttinen',
    author_email='jaakko.luttinen@iki.fi',
    description='BayesNet extension for Sphinx',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    package_data={'sphinxcontrib': ['tikz-bayesnet/tikzlibrarybayesnet.code.tex']},
#    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
