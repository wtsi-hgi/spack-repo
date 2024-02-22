# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemographic(RPackage):
	"""Providing Demographic Table with the P-Value, Standardized Mean
Difference Value

	The Demographic Table in R combines contingency table for categorical variables, mean and standard deviation for continuous variables. t-test, chi-square test and Fisher's exact test calculated the p-value of two groups. The standardized mean difference were performed with 95 % confident interval, and writing table into document file.
	"""
	
	cran = "demoGraphic" 

	version("0.1.0", md5="50f7af895cefe4f9b03f49f1ecb2809d")

	depends_on("r-officer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
