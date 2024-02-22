# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPfa(RPackage):
	"""Estimates False Discovery Proportion Under Arbitrary Covariance
Dependence

	Estimate the false discovery proportion (FDP) by Principal Factor Approximation method with general known and unknown covariance dependence.
	"""
	
	cran = "pfa" 

	version("1.1", md5="1a7a2f88c496b1dbb4b9b648c40390a2")

	depends_on("r-lars", type=("build", "run"))
	depends_on("r-poet", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
