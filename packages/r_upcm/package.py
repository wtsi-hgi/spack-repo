# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpcm(RPackage):
	"""Uncertainty in Partial Credit Models

	Provides an extension to the Partial Credit Model and Generalized Partial Credit Models which allows for an additional person parameter that characterizes the uncertainty of the person. The method was originally proposed by Tutz and Schauberger (2020) <doi:10.1177/0146621620920932>. 
	"""
	
	cran = "UPCM" 

	version("0.0-3", md5="b3c939f82006ae06b9b5ca0e740ff3fb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
