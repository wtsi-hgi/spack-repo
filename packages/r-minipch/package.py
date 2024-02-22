# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinipch(RPackage):
	"""Survival Distributions with Piece-Wise Constant Hazards

	Density, distribution function, ... hazard function, cumulative hazard function, survival function for survival distributions with piece-wise constant hazards and multiple states.
	"""
	
	homepage = "https://simnph.github.io/miniPCH/"
	cran = "miniPCH" 

	version("0.3.1", md5="dd7f1214a2e227d601827f9e9730e079")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
