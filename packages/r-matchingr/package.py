# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatchingr(RPackage):
	"""Matching Algorithms in R and C++

	Computes matching algorithms quickly using Rcpp.
    Implements the Gale-Shapley Algorithm to compute the stable
    matching for two-sided markets, such as the stable marriage
    problem and the college-admissions problem. Implements Irving's
    Algorithm for the stable roommate problem. Implements the top
    trading cycle algorithm for the indivisible goods trading problem.
	"""
	
	homepage = "https://github.com/jtilly/matchingR/"
	cran = "matchingR" 

	version("1.3.3", md5="53d58a244eb09e2ac12b0fd4fe9b8c0e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
