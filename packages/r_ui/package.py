# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUi(RPackage):
	"""Uncertainty Intervals and Sensitivity Analysis for Missing Data

	Implements functions to derive uncertainty intervals for (i) regression (linear and probit) parameters when outcome is missing not at random (non-ignorable missingness) introduced in Genbaeck, M., Stanghellini, E., de Luna, X. (2015) <doi:10.1007/s00362-014-0610-x> and Genbaeck, M., Ng, N., Stanghellini, E., de Luna, X. (2018) <doi:10.1007/s10433-017-0448-x>; and (ii) double robust and outcome regression estimators of average causal effects (on the treated) with possibly unobserved confounding introduced in Genbaeck, M., de Luna, X. (2018) <doi:10.1111/biom.13001>.
	"""
	
	cran = "ui" 

	version("0.1.1", md5="e0ffbfa0dc39e6be0fee3b12ff8cd340")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
