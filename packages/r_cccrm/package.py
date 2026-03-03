# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCccrm(RPackage):
	"""Concordance Correlation Coefficient for Repeated (and
Non-Repeated) Measures

	Estimates the Concordance Correlation Coefficient to assess agreement. The scenarios considered are non-repeated measures, non-longitudinal repeated measures (replicates) and longitudinal repeated measures. It also includes the estimation of the one-way intraclass correlation coefficient also known as reliability index. The estimation approaches implemented are variance components and U-statistics approaches. Description of methods can be found in Fleiss (1986) <doi:10.1002/9781118032923> and Carrasco et al. (2013) <doi:10.1016/j.cmpb.2012.09.002>.
	"""
	
	cran = "cccrm" 

	version("2.2.1", md5="a1d902b2c0fbd2971f19498a4620878d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
