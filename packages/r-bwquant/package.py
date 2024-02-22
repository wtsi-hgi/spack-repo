# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBwquant(RPackage):
	"""Bandwidth Selectors for Local Linear Quantile Regression

	Bandwidth selectors for local linear quantile regression, including cross-validation and plug-in methods. The local linear quantile regression estimate is also implemented.
	"""
	
	cran = "BwQuant" 

	version("0.1.0", md5="c89ef4ac607f23833992d63d07ff448f")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
