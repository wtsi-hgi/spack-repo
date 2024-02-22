# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzyranktests(RPackage):
	"""Fuzzy Rank Tests and Confidence Intervals

	Does fuzzy tests and confidence intervals (following Geyer
    and Meeden, Statistical Science, 2005, <doi:10.1214/088342305000000340>)
    for sign test and Wilcoxon signed rank and rank sum tests.
	"""
	
	homepage = "http://www.stat.umn.edu/geyer/fuzz/"
	cran = "fuzzyRankTests" 

	version("0.4", md5="8c54987d37104d55ea169bf9bea8d838")

	depends_on("r@3.0.2:", type=("build", "run"))
