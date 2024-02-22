# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReconstructkm(RPackage):
	"""Reconstruct Individual-Level Data from Published KM Plots

	Functions for reconstructing individual-level data (time, status, arm) from Kaplan-MEIER curves published in academic journals (e.g. NEJM, JCO, JAMA). The individual-level data can be used for re-analysis, meta-analysis, methodology development, etc. This package was used to generate the data for commentary such as Sun, Rich, & Wei (2018) <doi:10.1056/NEJMc1808567>. Please see the vignette for a quickstart guide. 
	"""
	
	cran = "reconstructKM" 

	version("0.3.0", md5="06f3294eaf3d23523bd64c199f329423")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
