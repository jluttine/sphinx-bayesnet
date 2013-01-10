# -*- coding: utf-8 -*-

# Copyright (C) 2011,2012 Jaakko Luttinen
#
# This file is licensed under Version 3.0 of the GNU General Public
# License.

import os, sys

DIR = os.path.abspath(os.path.dirname(__file__))
#SPHINX_TIKZ_DIR = os.path.join(DIR, 'sphinx-tikz')
#sys.path.insert(0, SPHINX_TIKZ_DIR)

from sphinxcontrib.tikz import TikzDirective, tikz_role

TIKZ_BAYESNET_FILE = os.path.join(DIR,
                                  'tikz-bayesnet/tikzlibrarybayesnet.code.tex')
bnfile = open(TIKZ_BAYESNET_FILE)
BAYESNET_DEFS = bnfile.read()
bnfile.close()

def bayesnet_role(role, rawtext, text, lineno, inliner, option={}, content=[]):
    # TODO: Add the BayesNet definitions to the content!
    return tikz_role(role, rawtext, text, lineno, inliner, option=option, content=content)

class BayesNetDirective(TikzDirective):
    def run(self):
        # Add TikZ libraries
        #self.options['libs'] = self.options.get('libs', '') + ',' + BAYESNET_LIBS
        # Run TikZ node
        (node,) = super(BayesNetDirective, self).run()
        # Add TikZ-BayesNet definitions
        node['tikz'] = BAYESNET_DEFS + node['tikz']
        return [node]

def setup(app):
    app.add_role('bayesnet', bayesnet_role)
    app.add_directive('bayesnet', BayesNetDirective)
