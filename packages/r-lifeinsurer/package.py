# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifeinsurer(RPackage):
	"""Modelling Traditional Life Insurance Contracts

	R6 classes to model traditional life insurance
    contracts like annuities, whole life insurances or endowments. Such life
    insurance contracts provide a guaranteed interest and are not directly linked
    to the performance of a particular investment vehicle, but they typically
    provide (discretionary) profit participation. This package provides a framework
    to model such contracts in a very generic (cash-flow-based) way and includes
    modelling profit participation schemes, dynamic increases or more general
    contract layers, as well as contract changes (like sum increases or premium
    waivers). All relevant quantities like premium decomposition, reserves and 
    benefits over the whole contract period are calculated and potentially 
    exported to 'Excel'. Mortality rates are given using the 'MortalityTables' package.
	"""
	
	homepage = "https://gitlab.open-tools.net/R/LifeInsureR"
	cran = "LifeInsureR" 

	version("1.0.0", md5="f99357ad1aff3f062091d1cc7a6a52ac")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-mortalitytables", type=("build", "run"))
	depends_on("r-objectproperties", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
