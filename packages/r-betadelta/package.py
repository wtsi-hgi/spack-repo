# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetadelta(RPackage):
	"""Confidence Intervals for Standardized Regression Coefficients

	Generates confidence intervals for standardized regression coefficients
    using delta method standard errors for models fitted by lm()
    as described in Yuan and Chan (2011) <doi:10.1007/s11336-011-9224-6>
    and Jones and Waller (2015) <doi:10.1007/s11336-013-9380-y>.
    A description of the package and code examples
    are presented in Pesigan, Sun, and Cheung (2023) <doi:10.1080/00273171.2023.2201277>.
	"""
	
	homepage = "https://github.com/jeksterslab/betaDelta"
	cran = "betaDelta" 

	version("1.0.4", md5="d46071a262ec301814734ab96be7f823")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
