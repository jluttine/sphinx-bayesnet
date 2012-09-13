sphinx-bayesnet
===============

This extension makes it easy to draw Bayesian networks and (directed)
factor graphs in Sphinx using TikZ syntax.  
The extension is based on a TikZ library called BayesNet. See
https://github.com/jluttine/tikz-bayesnet for more information.

This extension defines :code:`bayesnet` directive and role.

.. code-block::

   .. bayesnet::
      
      \node[latent]          (x) {$x$} ;
      \node[obs, below=of x] (y) {$y$} ;
      \edge {x} {y} ;

or the role as :code:`:bayesnet:\`\`\node[obs] {y}\`\``.

License
-------

Copyright (C) 2012 Jaakko Luttinen, Aalto University

Sphinx-BayesNet is licensed under Version 3.0 of the GNU General
Public License. See LICENSE file for a text of the license or visit
http://www.gnu.org/copyleft/gpl.html.

See the folders sphinx-tikz/ and tikz-bayesnet/ for their copyright
and license.
