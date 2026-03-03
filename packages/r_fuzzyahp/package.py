# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzyahp(RPackage):
	"""(Fuzzy) AHP Calculation

	Calculation of AHP (Analytic Hierarchy Process -
    <http://en.wikipedia.org/wiki/Analytic_hierarchy_process>)
    with classic and fuzzy weights based on Saaty's pairwise
    comparison method for determination of weights.
	"""
	
	homepage = "http://github.com/JanCaha/FuzzyAHP/"
	cran = "FuzzyAHP" 

	version("0.9.5", md5="d27b3cb2aa4fb78b5e07392981a05948")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
