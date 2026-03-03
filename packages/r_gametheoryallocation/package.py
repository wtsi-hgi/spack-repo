# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGametheoryallocation(RPackage):
	"""Tools for Calculating Allocations in Game Theory

	Many situations can be modeled as game theoretic situations. Some procedures are included in this package to calculate the most important allocations rules in Game Theory: Shapley value, Owen value or nucleolus, among other. First, we must define as an argument the value of the unions of the envolved agents with the characteristic function.   
	"""
	
	cran = "GameTheoryAllocation" 

	version("1.0", md5="19bc3f42ec3c06ffb640d003c18332ba")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
