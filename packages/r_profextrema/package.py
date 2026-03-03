# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfextrema(RPackage):
	"""Compute and Visualize Profile Extrema Functions

	Computes profile extrema functions for arbitrary functions. If the function is expensive-to-evaluate it computes profile extrema by emulating the function with a Gaussian process (using package 'DiceKriging'). In this case uncertainty quantification on the profile extrema can also be computed. The different plotting functions for profile extrema give the user a tool to better locate excursion sets. 
	"""
	
	cran = "profExtrema" 

	version("0.2.1", md5="45afbdeac4bba634254835cb5226bf0d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dicekriging", type=("build", "run"))
	depends_on("r-kriginv", type=("build", "run"))
	depends_on("r-pgpx", type=("build", "run"))
	depends_on("r-microbenchmark", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcdd", type=("build", "run"))
