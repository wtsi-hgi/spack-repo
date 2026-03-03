# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalot(RPackage):
	"""Optimal Transport Weights for Causal Inference

	Uses optimal transport distances to find probabilistic 
    matching estimators for causal inference.
    These methods are described in Dunipace, Eric (2021) <arXiv:2109.01991>.
    The package will build the weights, estimate treatment effects, and
    calculate confidence intervals via the methods described in the paper.
    The package also supports several other methods as described in the help 
    files.
	"""
	
	cran = "causalOT" 

	version("1.0.2", md5="7bb2c398aa5d75019ef6179f326f0d41")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cbps", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lbfgsb3c", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-osqp", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-torch", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
