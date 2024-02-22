# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInsurancerating(RPackage):
	"""Analytic Insurance Rating Techniques

	Methods for insurance rating. It helps actuaries to implement GLMs within all relevant steps needed to construct
 a risk premium from raw data. It provides a data driven strategy for the construction of insurance tariff classes.
 This strategy is based on the work by Antonio and Valdez (2012) <doi:10.1007/s10182-011-0152-7>. It also provides recipes
 on how to easily perform one-way, or univariate, analyses on an insurance portfolio. In addition it adds functionality
 to include reference categories in the levels of the coefficients in the output of a generalized linear regression analysis.
	"""
	
	homepage = "https://github.com/mharinga/insurancerating"
	cran = "insurancerating" 

	version("0.7.2", md5="7c6521a81ad5187babcf544cbeecd2d2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-citools", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dharma", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-evtree", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
