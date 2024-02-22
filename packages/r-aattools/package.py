# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAattools(RPackage):
	"""Reliability and Scoring Routines for the Approach-Avoidance Task

	Compute approach bias scores using different scoring algorithms,
    compute bootstrapped and exact split-half reliability estimates,
    and compute confidence intervals for individual participant scores.
	"""
	
	cran = "AATtools" 

	version("0.0.2", md5="bc59207786e9bc49167fd7d8af246b1c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
