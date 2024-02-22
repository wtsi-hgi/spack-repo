# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlouch(RPackage):
	"""Stochastic Linear Ornstein-Uhlenbeck Comparative Hypotheses

	An implementation of a phylogenetic comparative method. It can fit univariate among-species Ornstein-Uhlenbeck models of phenotypic trait evolution, where the trait evolves towards a primary optimum. The optimum can be modelled as a single parameter, as multiple discrete regimes on the phylogenetic tree, and/or with continuous covariates. See also Hansen (1997) <doi:10.2307/2411186>, Butler & King (2004) <doi:10.1086/426002>, Hansen et al. (2008) <doi:10.1111/j.1558-5646.2008.00412.x>.
	"""
	
	homepage = "https://github.com/kopperud/slouch"
	cran = "slouch" 

	version("2.1.5", md5="7bcff5ca20a9dcd9c9eddfc0b8b75dea")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
