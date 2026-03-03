# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiway(RPackage):
	"""Component Models for Multi-Way Data

	Fits multi-way component models via alternating least squares algorithms with optional constraints. Fit models include N-way Canonical Polyadic Decomposition, Individual Differences Scaling, Multiway Covariates Regression, Parallel Factor Analysis (1 and 2), Simultaneous Component Analysis, and Tucker Factor Analysis.
	"""
	
	cran = "multiway" 

	version("1.0-6", md5="638a22baa32e43f3096c613c370aa383")

	depends_on("r-cmls", type=("build", "run"))
