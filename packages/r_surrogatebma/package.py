# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurrogatebma(RPackage):
	"""Flexible Evaluation of Surrogate Markers with Bayesian Model
Averaging

	Provides functions to estimate the proportion of treatment effect explained by the surrogate marker using a Bayesian Model Averaging approach. Duan and Parast (2023) <doi:10.1002/sim.9986>.
	"""
	
	cran = "SurrogateBMA" 

	version("1.0", md5="0f12a76cd1c7d9797bf4eaa1f7394ac7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rsurrogate", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
