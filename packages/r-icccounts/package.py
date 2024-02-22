# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcccounts(RPackage):
	"""Intraclass Correlation Coefficient for Count Data

	Estimates the intraclass correlation coefficient (ICC) for count data to assess repeatability (intra-methods concordance) and concordance (between-method concordance). In the concordance setting, the ICC is equivalent to the concordance correlation coefficient estimated by variance components. The ICC is estimated using the estimates from generalized linear mixed models. The within-subjects distributions considered are: Poisson; Negative Binomial with additive and proportional extradispersion; Zero-Inflated Poisson; and Zero-Inflated Negative Binomial with additive and proportional extradispersion. The statistical methodology used to estimate the ICC with count data can be found in Carrasco (2010) <doi:10.1111/j.1541-0420.2009.01335.x>.
	"""
	
	cran = "iccCounts" 

	version("1.1.1", md5="4461d1044237d003503e712450770f55")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-glmmtmb", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
