# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtremefit(RPackage):
	"""Estimation of Extreme Conditional Quantiles and Probabilities

	Extreme value theory, nonparametric kernel estimation, tail
    conditional probabilities, extreme conditional quantile, adaptive estimation,
    quantile regression, survival probabilities.
	"""
	
	cran = "extremefit" 

	version("1.0.2", md5="f559f594bd2511dde8a7a62688be8d28")

	depends_on("r@2.10:", type=("build", "run"))
