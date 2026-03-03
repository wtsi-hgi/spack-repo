# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoutliers(RPackage):
	"""Outlier Detection and Influence Diagnostics for Meta-Analysis

	Computational tools for outlier detection and influence diagnostics of meta-analysis. Bootstrap distributions of the influence statistics are calculated, and the thresholds to determine outliers are explicitly provided.
	"""
	
	cran = "boutliers" 

	version("1.1-2", md5="c53eadd951709f69ecc3964ab36b2b48")

	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
