# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGregry(RPackage):
	"""GREGORY Estimation

	Functions which make using the Generalized Regression Estimator(GREG)
    J.N.K. Rao, Isabel Molina, (2015) <doi:10.3390/f11020244> 
    and the Generalized Regression Estimator Operating on Resolutions of Y (GREGORY) easier. 
    The functions are designed to work well within a forestry context, and estimate multiple 
    estimation units at once. Compared to other survey estimation packages, this function has greater flexibility when 
    describing the linear model.
	"""
	
	cran = "gregRy" 

	version("0.1.0", md5="af1e6b86f0e5907189f40bed2016fe2c")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
