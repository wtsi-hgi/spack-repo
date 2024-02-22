# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantilenpci(RPackage):
	"""Nonparametric Confidence Intervals for Quantiles

	Based on Alan D. Hutson (1999) <doi:10.1080/02664769922458>, "Calculating nonparametric confidence intervals for quantiles using fractional order statistics", Journal of Applied Statistics, 26:3, 343-353.
	"""
	
	cran = "QuantileNPCI" 

	version("0.9.0", md5="e6f6c6e5eed4bd2dbf53a612c865d54e")

	depends_on("r@2.10:", type=("build", "run"))
