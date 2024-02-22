# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBidimregression(RPackage):
	"""Calculates the Bidimensional Regression Between Two 2D
Configurations

	Calculates the bidimensional regression between two 2D configurations following the approach by Tobler (1965).
	"""
	
	homepage = "https://CRAN.R-project.org/package=BiDimRegression/"
	cran = "BiDimRegression" 

	version("2.0.1", md5="240bc0664259cbf86e90667910c9f66a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
