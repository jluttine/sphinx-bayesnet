sphinx-bayesnet
===============

This extension makes it easy to draw Bayesian networks and (directed)
factor graphs in Sphinx using TikZ syntax.  
The extension is based on a TikZ library called BayesNet. See
https://github.com/jluttine/tikz-bayesnet for more information.

This extension defines :code:`bayesnet` directive, which can be used
as:

.. code-block::

   .. bayesnet::
      
      \node[latent]          (x) {$x$} ;
      \node[obs, below=of x] (y) {$y$} ;
      \edge {x} {y} ;

The corresponding role has not yet been implemented.

License
-------

Copyright (C) 2012 Jaakko Luttinen, Aalto University

Sphinx-BayesNet is licensed under Version 3.0 of the GNU General
Public License.
