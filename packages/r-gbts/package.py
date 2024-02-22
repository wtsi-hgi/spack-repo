# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbts(RPackage):
	"""Hyperparameter Search for Gradient Boosted Trees

	An implementation of hyperparameter optimization for Gradient
    Boosted Trees on binary classification and regression problems. The current
    version provides two optimization methods: Bayesian optimization and random
    search. Instead of giving the single best model, the final output is an 
    ensemble of Gradient Boosted Trees constructed via the method of ensemble 
    selection.
	"""
	
	cran = "gbts" 

	version("1.2.0", md5="f8e1ac63fb4a7f201860d3837b1dba04")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
