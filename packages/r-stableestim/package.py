# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStableestim(RPackage):
	"""Estimate the Four Parameters of Stable Laws using Different
Methods

	Estimate the four parameters of stable laws using maximum
             likelihood method, generalised method of moments with
             finite and continuum number of points, iterative
             Koutrouvelis regression and Kogon-McCulloch method.  The
             asymptotic properties of the estimators (covariance
             matrix, confidence intervals) are also provided.
	"""
	
	homepage = "https://github.com/GeoBosh/StableEstim"
	cran = "StableEstim" 

	version("2.2", md5="b637815410cd17b0e408f02a53175917")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stabledist", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
