# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBde(RPackage):
	"""Bounded Density Estimation

	A collection of S4 classes which implements different methods to estimate and deal with densities in bounded domains. That is, densities defined within the interval [lower.limit, upper.limit], where lower.limit and upper.limit are values that can be set by the user.
	"""
	
	cran = "bde" 

	version("1.0.1.1", md5="99e7ce736017d9f9a1ce8b7b012b0187")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
