# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNatstrat(RPackage):
	"""Obtain Unweighted Natural Strata that Balance Many Covariates

	Natural strata can be used in observational studies to balance
    the distributions of many covariates across any number of treatment
    groups and any number of comparisons. These strata have proportional 
    amounts of units within each stratum across the treatments, allowing 
    for simple interpretation and aggregation across strata. Within each 
    stratum, the units are chosen using randomized rounding of a linear 
    program that balances many covariates.
    To solve the linear program, the 'Gurobi' commercial optimization software 
    is recommended, but not required. The 'gurobi' R package can be installed following the instructions 
    at <https://www.gurobi.com/documentation/9.1/refman/ins_the_r_package.html>.
	"""
	
	homepage = "https://github.com/kkbrum/natstrat"
	cran = "natstrat" 

	version("2.0.0", md5="2eb0b9952187c5ec56c7605b5e5c3fd5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-pps", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ramify", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
