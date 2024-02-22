# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNprobust(RPackage):
	"""Nonparametric Robust Estimation and Inference Methods using
Local Polynomial Regression and Kernel Density Estimation

	Tools for data-driven statistical analysis using local polynomial regression and kernel density estimation methods as described in Calonico, Cattaneo and Farrell (2018, <doi:10.1080/01621459.2017.1285776>): lprobust() for local polynomial point estimation and robust bias-corrected inference, lpbwselect() for local polynomial bandwidth selection, kdrobust() for kernel density point estimation and robust bias-corrected inference, kdbwselect() for kernel density bandwidth selection, and nprobust.plot() for plotting results. The main methodological and numerical features of this package are described in Calonico, Cattaneo and Farrell (2019, <doi:10.18637/jss.v091.i08>).
	"""
	
	cran = "nprobust" 

	version("0.4.0", md5="4406c88f000e5a4471497cb12389c951")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
