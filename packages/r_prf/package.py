# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrf(RPackage):
	"""Permutation Significance for Random Forests

	Estimate False Discovery Rates (FDRs) for importance metrics from
    random forest runs.
	"""
	
	cran = "pRF" 

	version("1.2", md5="81a2822676a95735df00e2160d25eadb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr@0.4.1:", type=("build", "run"))
	depends_on("r-multtest@2.25:", type=("build", "run"))
