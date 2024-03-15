# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalbatch(RPackage):
	"""Causal Batch Effects

	Software which provides numerous functionalities for detecting and removing group-level effects from high-dimensional scientific data which, when combined with additional assumptions, allow for causal conclusions, as-described in our manuscripts Bridgeford et al. (2024) <doi:10.1101/2021.09.03.458920> and Bridgeford et al. (2023) <arXiv:2307.13868>. Also provides a number of useful utilities for generating simulations and balancing covariates across multiple groups/batches of data via matching and propensity trimming for more than two groups.
	"""
	
	homepage = "https://github.com/neurodata/causal_batch"
	cran = "causalBatch" 

	version("1.2.0", md5="c5823bdbae72e6094b0fe85e6111cd20")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-cdcsis", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-matchit", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
