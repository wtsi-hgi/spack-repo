# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogitnorm(RPackage):
	"""Functions for the Logitnormal Distribution

	Density, distribution, quantile and random generation function for the logitnormal distribution. Estimation of the mode and the first two moments. Estimation of distribution parameters.
	"""
	
	cran = "logitnorm" 

	version("0.8.39", md5="1d08b2f259ce83e21ab7542212518eb9")

