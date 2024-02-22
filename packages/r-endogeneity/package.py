# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REndogeneity(RPackage):
	"""Recursive Two-Stage Models to Address Endogeneity

	Various recursive two-stage models to address the endogeneity issue of treatment variables in observational study or mediators in experiments. The details of the models are discussed in Peng (2023) <doi:10.1287/isre.2022.1113>. 
	"""
	
	cran = "endogeneity" 

	version("2.1.3", md5="a5a477fe20e70a09f0870c5c48a605b4")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
