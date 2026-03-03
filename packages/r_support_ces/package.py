# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupportCes(RPackage):
	"""Basic Functions for Supporting an Implementation of Choice
Experiments

	Provides basic functions that support an implementation of (discrete) choice experiments (CEs). CEs is a question-based survey method measuring people's preferences for goods/services and their characteristics. Refer to Louviere et al. (2000) <doi:10.1017/CBO9780511753831> for details on CEs, and Aizaki (2012) <doi:10.18637/jss.v050.c02> for the package.
	"""
	
	cran = "support.CEs" 

	version("0.7-0", md5="a502613e060d28695c2a718a5e90e50d")

	depends_on("r-doe-base", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-simex", type=("build", "run"))
