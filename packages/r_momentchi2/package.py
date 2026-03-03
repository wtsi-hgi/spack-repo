# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMomentchi2(RPackage):
	"""Moment-Matching Methods for Weighted Sums of Chi-Squared Random
Variables

	A collection of moment-matching methods for computing the cumulative distribution function of a positively-weighted sum of chi-squared random variables. Methods include the Satterthwaite-Welch method, Hall-Buckley-Eagleson method, Wood's F method, and the Lindsay-Pilla-Basak method.
	"""
	
	cran = "momentchi2" 

	version("0.1.5", md5="d7cac1b16db972c52ffb0a29cc26aefe", url="https://cran.r-project.org/src/contrib/momentchi2_0.1.5.tar.gz")

	depends_on("r@3.1.2:", type=("build", "run"))
