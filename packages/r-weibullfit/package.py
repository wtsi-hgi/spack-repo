# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeibullfit(RPackage):
	"""Fits and Plots a Dataset to the Weibull Probability Distribution
Function

	Provides a single function to fit data of an input data frame into one of the selected Weibull functions (w2, w3 and it's truncated versions), calculating the scale, location and shape parameters accordingly. The resulting plots and files are saved into the 'folder' parameter provided by the user. References: a) John C. Nash, Ravi Varadhan (2011). "Unifying Optimization Algorithms to Aid Software System Users: optimx for R" <doi:10.18637/jss.v043.i09>.
	"""
	
	cran = "WeibullFit" 

	version("0.1.0", md5="889f16178a64360dbe3dd4786f498422")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-r-oo", type=("build", "run"))
	depends_on("r-fadist", type=("build", "run"))
	depends_on("r-mixdist", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-ksamples", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
