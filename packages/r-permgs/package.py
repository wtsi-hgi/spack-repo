# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPermgs(RPackage):
	"""Permutational Group Sequential Test for Time-to-Event Data

	Permutational group-sequential tests for time-to-event data based on the log-rank test statistic. Supports exact permutation test when the censoring distributions are equal in the treatment and the control group and approximate imputation-permutation methods when the censoring distributions are different. 
	"""
	
	cran = "permGS" 

	version("0.2.5", md5="ed5151af97a521defe5cb15129325a0e")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
