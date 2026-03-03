# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcminification(RPackage):
	"""Random Coefficient Minification Time Series Models

	Data sets, and functions for simulating and fitting nonlinear time series with minification and nonparametric models.
	"""
	
	cran = "RCMinification" 

	version("1.2", md5="181823e31f6cb13847b968a1150e4e64")

	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-locpol", type=("build", "run"))
