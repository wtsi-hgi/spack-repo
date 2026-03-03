# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitter(RPackage):
	"""Fit Hundreds of Theoretical Distributions to Empirical Data

	Systematic fit of hundreds of theoretical univariate distributions to empirical data via maximum likelihood estimation. Fits are reported and summarized by a data.frame, a csv file or a 'shiny' app (here with additional features like visual representation of fits). All output formats provide assessment of goodness-of-fit by the following methods: Kolmogorov-Smirnov test, Shapiro-Wilks test, Anderson-Darling test.
	"""
	
	cran = "fitteR" 

	version("0.2.0", md5="b0ea52a8c199df1a34ec7828287f69a6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
