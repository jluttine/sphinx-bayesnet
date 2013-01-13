Installation
============

Install from PyPI:

.. code-block:: console

   pip install sphinxcontrib-bayesnet

Or install the required packages and the latest development version
from Github:

.. code-block:: console

   pip install sphinxcontrib-tikz
   git clone --recursive https://github.com/jluttine/sphinx-bayesnet.git
   cd sphinx-bayesnet
   git submodule update --init
   python setup.py install

In order to use the extension, you need to modify the file ``conf.py``
to contain the following definitions:

.. code-block:: console

   extensions = ['sphinxcontrib.tikz',
                 'sphinxcontrib.bayesnet']

   latex_elements = {
   'preamble': r'\usepackage{tikz}',
   }

