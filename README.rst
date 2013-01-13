=============================
BayesNet Extension for Sphinx
=============================

Introduction
============

This extension makes it easy to draw Bayesian networks and (directed)
factor graphs in Sphinx using TikZ syntax.  The extension is based on
a TikZ library called BayesNet
(https://github.com/jluttine/tikz-bayesnet).

This extension defines :code:`bayesnet` directive, which can be used
as:

.. code-block:: latex

   .. bayesnet::
      
      \node[latent]          (x) {$x$} ;
      \node[obs, below=of x] (y) {$y$} ;
      \edge {x} {y} ;

The corresponding role has not yet been implemented.

License
=======

Copyright (C) 2012-2013 Jaakko Luttinen jaakko.luttinen@iki.fi, Aalto University

This extension is licensed under Version 3.0 of the GNU General Public
License.
