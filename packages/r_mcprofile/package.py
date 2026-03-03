# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcprofile(RPackage):
	"""Testing Generalized Linear Hypotheses for Generalized Linear
Model Parameters by Profile Deviance

	Calculation of signed root deviance profiles for linear combinations of parameters in a generalized linear model. Multiple tests and simultaneous confidence intervals are provided.
	"""
	
	cran = "mcprofile" 

	version("1.0-1", md5="77af928f94a79d85bf929a03dc0ffc95")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
