# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package constains the "bayesnet" Sphinx extension which makes it
easy to draw Bayesian networks, graphical models and (directed) factor
graphs in Sphinx using TikZ syntax. The extension is based on a TikZ
library called BayesNet.
'''

requires = ['Sphinx>=0.6',
            'sphinxcontrib-tikz']#>=0.4

setup(
    name='sphinxcontrib-bayesnet',
    version='0.1',
    url='http://bitbucket.org/birkenfeld/sphinx-contrib',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-bayesnet',
    author='Jaakko Luttinen',
    author_email='jaakko.luttinen@iki.fi',
    description='Sphinx "bayesnet" extension',
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
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
    use_2to3=True,
)
