# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDwp(RPackage):
	"""Density-Weighted Proportion

	Fit a Poisson regression to carcass distance data and integrate over the searched area at a wind farm to estimate the fraction of carcasses falling in the searched area and format the output for use as the dwp parameter in the 'GenEst' or 'eoa' package for estimating bird and bat mortality, following Dalthorp, et al. (2022) <arXiv:2201.10064>.
	"""
	
	cran = "dwp" 

	version("1.1", md5="71c07a837b0500336433db6459b5e735")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-expint", type=("build", "run"))
	depends_on("r-genest", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-invgamma", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
