# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongitudinalanal(RPackage):
	"""Longitudinal Data Analysis

	Regression analysis of mixed sparse synchronous and asynchronous longitudinal covariates. Please cite the manuscripts corresponding to this package: Sun, Z. et al. (2023) <arXiv:2305.17715>  and  Liu, C. et al. (2023) <arXiv:2305.17662>.
	"""
	
	cran = "longitudinalANAL" 

	version("0.2", md5="9e8d3d3d94e02214beeb98ec96895f45")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dlm", type=("build", "run"))
