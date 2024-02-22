# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormdata(RPackage):
	"""Derivation of Regression-Based Normative Data

	Normative data are often used to estimate the relative position of a raw test score in the population. This package allows for deriving regression-based normative data. It includes functions that enable the fitting of regression models for the mean and residual (or variance) structures, test the model assumptions, derive the normative data in the form of normative tables or automatic scoring sheets, and estimate confidence intervals for the norms. This package accompanies the book Van der Elst, W. (2024). Regression-based normative data for psychological assessment. A hands-on approach using R. Springer Nature.  
	"""
	
	cran = "NormData" 

	version("1.0", md5="8dc8693e77c10b834908cc6d987001d2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-doby", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
