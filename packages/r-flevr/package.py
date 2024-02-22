# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlevr(RPackage):
	"""Flexible, Ensemble-Based Variable Selection with Potentially
Missing Data

	Perform variable selection in settings with possibly missing data
    based on extrinsic (algorithm-specific) and intrinsic (population-level)
    variable importance. Uses a Super Learner ensemble to estimate the
    underlying prediction functions that give rise to estimates of variable importance. For more information about the methods, please see Williamson and Huang (2023+) <arXiv:2202.12989>.
	"""
	
	homepage = "https://github.com/bdwilliamson/flevr"
	cran = "flevr" 

	version("0.0.4", md5="07d59f9c0595a6a399675d1c275e8877")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
