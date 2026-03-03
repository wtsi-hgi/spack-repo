# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVirf(RPackage):
	"""Computation of Volatility Impulse Response Function of
Multivariate Time Series

	Computation of volatility impulse response function for multivariate time series model using algorithm by Jin, Lin and Tamvakis (2012) <doi.org/10.1016/j.eneco.2012.03.003>.
	"""
	
	cran = "VIRF" 

	version("0.1.0", md5="7b20f31ae9ca5d7c2d073360428a2e29")

	depends_on("r-rmgarch", type=("build", "run"))
	depends_on("r-mgarchbekk", type=("build", "run"))
	depends_on("r-gnm", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-bigvar", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-matlib", type=("build", "run"))
