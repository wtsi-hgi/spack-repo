# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmathresh(RPackage):
	"""Thresholds and Invariant Intervals for Network Meta-Analysis

	Calculation and presentation of decision-invariant bias adjustment
    thresholds and intervals for Network Meta-Analysis, as described by 
    Phillippo et al. (2018) <doi:10.1111/rssa.12341>. These describe the 
    smallest changes to the data that would result in a change of decision.
	"""
	
	cran = "nmathresh" 

	version("0.1.6", md5="c9ddd1ac2455c5ff96bf197a0557fe42")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
