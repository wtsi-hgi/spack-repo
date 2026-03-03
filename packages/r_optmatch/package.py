# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptmatch(RPackage):
	"""Functions for Optimal Matching

	Distance based bipartite matching using minimum cost flow, oriented
    to matching of treatment and control groups in observational studies ('Hansen'
    and 'Klopfer' 2006 <doi:10.1198/106186006X137047>). Routines are provided to
    generate distances from generalised linear models (propensity score
    matching), formulas giving variables on which to limit matched distances,
    stratified or exact matching directives, or calipers, alone or in
    combination.
	"""
	
	homepage = "http://optmat.ch"
	cran = "optmatch" 

	version("0.10.7", md5="26d2ef57a8724f84b5609eb95be70b62")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlemon", type=("build", "run"))
