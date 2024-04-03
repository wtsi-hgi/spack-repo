# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedprobr(RPackage):
	"""Probability Computations on Pedigrees

	An implementation of the Elston-Stewart algorithm for
    calculating pedigree likelihoods given genetic marker data (Elston and
    Stewart (1971) <doi:10.1159/000152448>). The standard algorithm is
    extended to allow inbred founders. 'pedprobr' is part of the 'ped
    suite', a collection of packages for pedigree analysis in R. In
    particular, 'pedprobr' depends on 'pedtools' for pedigree
    manipulations and 'pedmut' for mutation modelling. For more
    information, see 'Pedigree Analysis in R' (Vigeland, 2021,
    ISBN:9780128244302).
	"""
	
	homepage = "https://github.com/magnusdv/pedprobr"
	cran = "pedprobr" 

	version("0.9.3", md5="af7d78d3c4804153959bb8f7d1ec79b7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-pedtools@1.1:", type=("build", "run"))
	depends_on("r-pedmut@0.5:", type=("build", "run"))
