# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptrefine(RPackage):
	"""Optimally Refine Strata

	Splits initial strata into refined strata that optimize covariate balance. For more information, please email the author for a copy of the accompanying manuscript. To solve the linear program, the 'Gurobi' commercial optimization software is recommended, but not required. The 'gurobi' R package can be installed following the instructions at <https://www.gurobi.com/documentation/9.1/refman/ins_the_r_package.html>.
	"""
	
	homepage = "https://github.com/kkbrum/optrefine"
	cran = "optrefine" 

	version("1.1.0", md5="d8f839237c0261b35f01ddb36176ed91")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
