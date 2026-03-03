# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitultd(RPackage):
	"""Fit Univariate Mixed and Usual Distributions

	Extends the fitdist() (from 'fitdistrplus') adding the Anderson-Darling ad.test() (from 'ADGofTest') and Kolmogorov Smirnov Test ks.test() inside, trying the distributions from 'stats' package by default and offering a second function which uses mixed distributions to fit, this distributions are split with unsupervised learning, with Mclust() function (from 'mclust').
	"""
	
	homepage = "https://github.com/jcval94/FitUltD"
	cran = "FitUltD" 

	version("3.1.0", md5="69316221d94de9ce256ae67097ffda4b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-adgoftest", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
