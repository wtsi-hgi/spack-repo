# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCctools(RPackage):
	"""Tools for the Continuous Convolution Trick in Nonparametric
Estimation

	Implements the uniform scaled beta distribution and
  the continuous convolution kernel density estimator.
	"""
	
	cran = "cctools" 

	version("0.1.2", md5="2855ea739c0db8fe5c92aeb63bdd1900")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-qrng", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
