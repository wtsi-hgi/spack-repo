# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZipbayes(RPackage):
	"""Bayesian Methods in the Analysis of Zero-Inflated Poisson Model

	Implementation of zero-inflated Poisson models under Bayesian framework using data augmentation as discussed in Chapter 5 of Zhang (2020) <https://hdl.handle.net/10012/16378>. This package is constructed in accommodating four different scenarios: the general scenario, the scenario with measurement error in responses, the external validation scenario, and the internal validation scenario.
	"""
	
	cran = "ZIPBayes" 

	version("1.0.2", md5="0945e9330f2d77a9be3c5fa893a0c32f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
