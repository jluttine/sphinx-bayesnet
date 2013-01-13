Example
=======

::
   
   .. bayesnet::

      \node[obs] (y) {$y$};
      \node[latent, above left=of y] (mu) {$\mu$};
      \node[latent, above right=of y] (sigma) {$\sigma$};
      \edge{mu,sigma}{y};
      \plate {} {(y)} {$N$};

.. bayesnet::

   \node[obs] (y) {$y$};
   \node[latent, above left=of y] (mu) {$\mu$};
   \node[latent, above right=of y] (sigma) {$\sigma$};
   \edge{mu,sigma}{y};
   \plate {} {(y)} {$N$};
