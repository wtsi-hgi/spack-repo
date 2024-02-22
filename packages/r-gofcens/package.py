# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGofcens(RPackage):
	"""Goodness-of-Fit Methods for Right-Censored Data

	Graphical tools and goodness-of-fit tests for right-censored data:
             1. Kolmogorov-Smirnov, Crámer-von Mises, and Anderson-Darling tests
                based on the empirical distribution function for complete data and their 
                extensions  for  right-censored data. 
             2. Generalized chi-squared-type tests  based on the squared difference between 
                observed and expected counts using random cells with right-censored data.
             3. A series of graphical tools such as probability or cumulative hazard 
                plots to guide the decision about the parametric model that best
                fits the data.
	"""
	
	cran = "GofCens" 

	version("0.92", md5="acc9e33592200e570932d77d81516495")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-survsim", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
