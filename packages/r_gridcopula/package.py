# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGridcopula(RPackage):
	"""Bivariate Copula Functions Based on Regular Grid

	Estimates grid type bivariate copula functions, calculates some association measures and provides several copula graphics.
	"""
	
	cran = "GRIDCOPULA" 

	version("1.0.0", md5="7196f50621f55e5d1623636ff034bfcb")

	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
