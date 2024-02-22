# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetgen(RPackage):
	"""Stochastic Weather Generator

	An adaptation of the multi-variable stochastic weather generator proposed in 'Rglimclim' to perform gap-filling and temporal extension at sub-daily resolution. Simulation is performed based on large scale variables and climatic observation data that could be generated from different gauged stations having geographical proximity. SWG relies on reanalyses. Multi-variable dependence is taking into account by using the decomposition of the product rule (in statistics) into conditional probabilities. See <https://hal.archives-ouvertes.fr/hal-02554676>.
	"""
	
	homepage = "www.r-project.org"
	cran = "MetGen" 

	version("0.5", md5="216518de79b59fdc022eb57941b7cf6d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
