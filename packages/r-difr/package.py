# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDifr(RPackage):
	"""Collection of Methods to Detect Dichotomous Differential Item
Functioning (DIF)

	Provides a collection of standard methods to detect differential item functioning among dichotomously scored items. Methods for uniform and non-uniform DIF, based on test-score or IRT methods, for comparing two or more than two groups of respondents, are available (Magis, Beland, Tuerlinckx and De Boeck,A General Framework and an R Package for the Detection of Dichotomous Differential Item Functioning, Behavior Research Methods, 42, 2010, 847-862 <doi:10.3758/BRM.42.3.847>).
	"""
	
	cran = "difR" 

	version("5.1", md5="fc27c85882d98beb2493f05e4a6e4f11")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-deltaplotr", type=("build", "run"))
