# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNparld(RPackage):
	"""Nonparametric Analysis of Longitudinal Data in Factorial
Experiments

	Performs nonparametric
        analysis of longitudinal data in factorial experiments.
        Longitudinal data are those which are collected from the same
        subjects over time, and they frequently arise in biological
        sciences. Nonparametric methods do not require distributional
        assumptions, and are applicable to a variety of data types
        (continuous, discrete, purely ordinal, and dichotomous).  Such
        methods are also robust with respect to outliers and for small
        sample sizes.
	"""
	
	cran = "nparLD" 

	version("2.2", md5="0379bdadd8bec51e2e8dbe6110cd0ddf")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
