# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcostats(RPackage):
	"""Code and Data Accompanying the Eco-Stats Text (Warton 2022)

	Functions and data supporting the Eco-Stats text (Warton, 2022, Springer), and solutions to exercises. Functions include tools for using simulation envelopes in diagnostic plots, and a function for diagnostic plots of multivariate linear models. Datasets mentioned in the package are included here (where not available elsewhere) and there is a vignette for each chapter of the text with solutions to exercises.
	"""
	
	cran = "ecostats" 

	version("1.1.11", md5="2353a2b540f8647f4e366923d82f2ba0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvabund@4.2:", type=("build", "run"))
	depends_on("r-ecocopula", type=("build", "run"))
	depends_on("r-get", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
