# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApt(RPackage):
	"""Asymmetric Price Transmission

	Asymmetric price transmission between two time series is assessed. Several functions are available for linear and nonlinear threshold cointegration, and furthermore, symmetric and asymmetric error correction model.
	"""
	
	cran = "apt" 

	version("3.0", md5="9ea2bcf1abecbf06c0d3c04df684848b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-erer", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
