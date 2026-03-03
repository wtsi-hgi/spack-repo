# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSadists(RPackage):
	"""Some Additional Distributions

	Provides the density, distribution, quantile and generation functions of some obscure probability 
    distributions, including the doubly non-central t, F, Beta, and Eta distributions; 
    the lambda-prime and K-prime; the upsilon distribution; the (weighted) sum of 
    non-central chi-squares to a power; the (weighted) sum of log non-central chi-squares;
    the product of non-central chi-squares to powers; the product of doubly non-central
    F variables; the product of independent normals.
	"""
	
	homepage = "https://github.com/shabbychef/sadists"
	cran = "sadists" 

	version("0.2.5", md5="c6e2f1b3fe96ebef51b3917518408d2f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-pdqutils@0.1.1:", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
