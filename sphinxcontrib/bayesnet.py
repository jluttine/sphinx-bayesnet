# -*- coding: utf-8 -*-

# Copyright (C) 2011,2012 Jaakko Luttinen
#
# This file is licensed under Version 3.0 of the GNU General Public
# License.

import os, sys

from sphinxcontrib.tikz import TikzDirective, tikz_role

def bayesnet_role(role, rawtext, text, lineno, inliner, option={}, content=[]):
    # TODO: Add the BayesNet definitions to the content!
    return tikz_role(role, rawtext, text, lineno, inliner, option=option, content=content)

class BayesNetDirective(TikzDirective):
    def run(self):
        # Add TikZ libraries
        libs = self.options.get("libs", "")
        self.options["libs"] = (
            "bayesnet" if libs == "" else
            libs + ",bayesnet"
        )
        # Run TikZ node
        (node,) = super(BayesNetDirective, self).run()
        return [node]

def setup(app):
    app.add_role('bayesnet', bayesnet_role)
    app.add_directive('bayesnet', BayesNetDirective)
