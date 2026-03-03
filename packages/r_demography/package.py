# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemography(RPackage):
	"""Forecasting Mortality, Fertility, Migration and Population Data

	Functions for demographic analysis including lifetable
        calculations; Lee-Carter modelling; functional data analysis of
        mortality rates, fertility rates, net migration numbers; and
        stochastic population forecasting.
	"""
	
	homepage = "https://pkg.robjhyndman.com/demography/"
	cran = "demography" 

	version("2.0", md5="0efd82da9f4c4158232fbcf184a2cef9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-forecast@8.5:", type=("build", "run"))
	depends_on("r-ftsa@4.8:", type=("build", "run"))
	depends_on("r-rainbow", type=("build", "run"))
	depends_on("r-cobs", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-hmdhfdplus@2:", type=("build", "run"))
