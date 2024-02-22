# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountgmifs(RPackage):
	"""Discrete Response Regression for High-Dimensional Data

	Provides a function for fitting Poisson and negative binomial regression models when the number of parameters exceeds the sample size, using the the generalized monotone incremental forward stagewise method.
	"""
	
	cran = "countgmifs" 

	version("0.0.2", md5="91b3e903315fe439bf54e5ebcbc9ddad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
