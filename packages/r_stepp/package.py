# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepp(RPackage):
	"""Subpopulation Treatment Effect Pattern Plot (STEPP)

	A method to explore the treatment-covariate interactions in survival or generalized 
	linear model (GLM) for continuous, binomial and count data arising from two or more treatment 
	arms of a clinical trial. A permutation distribution approach to inference is implemented, 
	based on permuting the covariate values within each treatment group.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "stepp" 

	version("3.2.6", md5="c2c24d2668d3d83310c2e4d5ef9c9452")

	depends_on("r-car", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
