# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RControltest(RPackage):
	"""Quantile Comparison for Two-Sample Right-Censored Survival Data

	Nonparametric two-sample procedure for comparing survival quantiles.
	"""
	
	cran = "controlTest" 

	version("1.1.0", md5="d150af70884ab2c57f90cd57a177eee0")

	depends_on("r-survival@2.41:", type=("build", "run"))
