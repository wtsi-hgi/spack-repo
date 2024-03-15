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

	version("0.3.2", md5="dfc8ce54027a25e09d281f7eeccd884c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
