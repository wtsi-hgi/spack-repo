# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynamac(RPackage):
	"""Dynamic Simulation and Testing for Single-Equation ARDL Models

	While autoregressive distributed lag (ARDL) models allow for extremely flexible dynamics, interpreting substantive significance of complex lag structures remains difficult. This package is designed to assist users in dynamically simulating and plotting the results of various ARDL models. It also contains post-estimation diagnostics, including a test for cointegration when estimating the error-correction variant of the autoregressive distributed lag model (Pesaran, Shin, and Smith 2001 <doi:10.1002/jae.616>).
	"""
	
	homepage = "https://github.com/andyphilips/dynamac/"
	cran = "dynamac" 

	version("0.1.12", md5="d151c1859d30bec39400e1dc4c917785")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
