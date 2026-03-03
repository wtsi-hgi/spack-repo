# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdftest(RPackage):
	"""Goodness of Fit Based on Empirical Distribution Function

	This repository contains software for the calculation of goodness-of-fit test statistics and their P-values. The three statistics computed are the Empirical Distribution function statistics called Cramer-von Mises, Anderson-Darling, and Watson statistics. The statistics and their P-values can be used to assess an assumed distribution.The following distributions are available: Uniform, Normal, Gamma, Logistic, Laplace, Weibull, Extreme Value, and Exponential.
	"""
	
	cran = "EDFtest" 

	version("0.1.0", md5="7bff2781cbd445b2840303f6a55f6d10")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-compquadform@1.4.3:", type=("build", "run"))
	depends_on("r-rmutil@1.1.5:", type=("build", "run"))
