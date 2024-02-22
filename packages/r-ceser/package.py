# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCeser(RPackage):
	"""Cluster Estimated Standard Errors

	Implementation of the Cluster Estimated Standard Errors (CESE) proposed in Jackson (2020) <DOI:10.1017/pan.2019.38> to compute clustered standard errors of linear coefficients in regression models with grouped data.
	"""
	
	homepage = "https://github.com/DiogoFerrari/ceser"
	cran = "ceser" 

	version("1.0.0", md5="49875c03457408df7b9cc1499b2d5080")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
