# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGselection(RPackage):
	"""Genomic Selection

	Genomic selection is a specialized form of marker assisted selection. The package contains functions to select important genetic markers and predict phenotype on the basis of fitted training data using integrated model framework (Guha Majumdar et. al. (2019) <doi:10.1089/cmb.2019.0223>) developed by combining one additive (sparse additive models by Ravikumar et. al. (2009) <doi:10.1111/j.1467-9868.2009.00718.x>) and one non-additive (hsic lasso by Yamada et. al. (2014) <doi:10.1162/NECO_a_00537>) model.
	"""
	
	cran = "GSelection" 

	version("0.1.0", md5="61a7b03c54ed477875bbb74f3388e12a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sam", type=("build", "run"))
	depends_on("r-penalized", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
