# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHctrial(RPackage):
	"""Using Historical Controls for Designing Phase II Clinical Trials

	Provides functions for designing phase II clinical trials adjusting for the heterogeneity of the population using known subgroups or historical controls.
	"""
	
	cran = "hctrial" 

	version("0.1.0", md5="cb09abc55729656178a47191684d9e36")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-clinfun", type=("build", "run"))
	depends_on("r-genbinomapps", type=("build", "run"))
