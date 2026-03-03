# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcmr(RPackage):
	"""Gaussian Copula Marginal Regression

	Likelihood inference in Gaussian copula marginal
        regression models.
	"""
	
	cran = "gcmr" 

	version("1.0.3", md5="5bfc042d1eb3a8f8f0fe14447dda5556")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
