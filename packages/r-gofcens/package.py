# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGofcens(RPackage):
	"""Goodness-of-Fit Methods for Complete and Right-Censored Data

	Graphical tools and goodness-of-fit tests for complete and right-censored data:
             1. Kolmogorov-Smirnov, Cramér-von Mises, and Anderson-Darling tests,
                which use the empirical distribution function for complete data 
                and are extended for right-censored data.
             2. Generalized chi-squared-type test, which is based on the squared 
                differences between observed and expected counts using random 
                cells with right-censored data.
             3. A series of graphical tools such as probability or cumulative hazard 
                plots to guide the decision about the most suitable parametric model 
                for the data.
	"""
	
	cran = "GofCens" 

	version("0.98", md5="34b042aec4cfbcb86a62223059aca567")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-survsim", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
