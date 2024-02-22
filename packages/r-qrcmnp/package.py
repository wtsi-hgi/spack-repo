# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrcmnp(RPackage):
	"""Nonlinear and Penalized Quantile Regression Coefficients
Modeling

	Nonlinear and Penalized parametric modeling of quantile regression coefficient functions. Sottile G, Frumento P, Chiodi M and Bottai M (2020) <doi:10.1177/1471082X19825523>.
	"""
	
	cran = "qrcmNP" 

	version("0.2.1", md5="6ad0a9a74b9995a2734ab28c8b6f6472")

	depends_on("r-survival@2.4.1:", type=("build", "run"))
	depends_on("r-qrcm@3:", type=("build", "run"))
