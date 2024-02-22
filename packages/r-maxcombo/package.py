# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaxcombo(RPackage):
	"""The Group Sequential Max-Combo Test for Comparing Survival
Curves

	Functions for comparing survival curves using the max-combo test at a single timepoint or repeatedly at successive respective timepoints while controlling type I error (i.e., the group sequential setting), as published by Prior (2020) <doi:10.1177/0962280220931560>.  The max-combo test is a generalization of the weighted log-rank test, which itself is a generalization of the log-rank test, which is a commonly used statistical test for comparing survival curves, e.g., during or after a clinical trial as part of an effort to determine if a new drug or therapy is more effective at delaying undesirable outcomes than an established drug or therapy or a placebo.
	"""
	
	cran = "maxcombo" 

	version("1.0", md5="df1da737a620e3a46f202d3dd841ebe9")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mstate", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
