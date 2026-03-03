# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShuffleci(RPackage):
	"""Confidence Intervals Compared via Shuffling

	Scripts and exercises that use card shuffling to teach confidence interval comparisons for different estimators.
	"""
	
	cran = "shuffleCI" 

	version("0.1.0", md5="f8cdb50e89e4abd691db35dcc38b6d30")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
