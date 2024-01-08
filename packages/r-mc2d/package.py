# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RMc2d(RPackage):
	"""Tools for Two-Dimensional Monte-Carlo Simulations

	A complete framework to build and study Two-Dimensional Monte-Carlo simulations, aka Second-Order Monte-Carlo simulations. Also includes various distributions (pert, triangular, Bernoulli, empirical discrete and continuous).
	"""
	
	cran = "mc2d" 

	version("0.2.0", md5="d8127ac363842b9e7ac785f499700390")

	depends_on("r@2.10.0:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
