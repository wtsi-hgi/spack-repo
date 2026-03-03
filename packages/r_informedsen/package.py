# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInformedsen(RPackage):
	"""Sensitivity Analysis Informed by a Test for Bias

	After testing for biased treatment assignment in an observational study using an unaffected outcome, the sensitivity analysis is constrained to be compatible with that test.  The package uses the optimization software gurobi obtainable from <https://www.gurobi.com/>, together with its associated R package, also called gurobi; see: <https://www.gurobi.com/documentation/7.0/refman/installing_the_r_package.html>.  The method is a substantial computational and practical enhancement of a concept introduced in Rosenbaum (1992) Detecting bias with confidence in observational studies Biometrika, 79(2), 367-374  <doi:10.1093/biomet/79.2.367>.
	"""
	
	cran = "informedSen" 

	version("1.0.7", md5="346a7e946f5215c6be8caec7fba66341")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sensitivitymult", type=("build", "run"))
