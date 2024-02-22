# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondmvnorm(RPackage):
	"""Conditional Multivariate Normal Distribution

	Computes conditional multivariate normal densities, probabilities, and random deviates.
	"""
	
	cran = "condMVNorm" 

	version("2020.1", md5="0d2b112deb016ad68348962300447c26")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
