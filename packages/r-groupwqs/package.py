# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGroupwqs(RPackage):
	"""Grouped Weighted Quantile Sum Regression

	Fits weighted quantile sum (WQS) regressions for one or more chemical groups with continuous or binary outcomes. Wheeler D, Czarnota J.(2016) <doi:10.1289/isee.2016.4698>.
	"""
	
	cran = "groupWQS" 

	version("0.0.3", md5="d24a9a7930102cada194a538cdd050d8")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
