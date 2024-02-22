# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuadrupen(RPackage):
	"""Sparsity by Worst-Case Quadratic Penalties

	Fits classical sparse regression models with
    efficient active set algorithms by solving quadratic problems as described by 
    Grandvalet, Chiquet and Ambroise (2017) <arXiv:1210.2077>. Also provides a few 
    methods for model selection purpose (cross-validation, stability selection).
	"""
	
	homepage = "https://github.com/jchiquet/quadrupenCRAN"
	cran = "quadrupen" 

	version("0.2-11", md5="2d3fa1bfc227fd848f60b72d90c1bbca")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
