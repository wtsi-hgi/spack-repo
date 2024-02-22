# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmalschains(RPackage):
	"""Continuous Optimization using Memetic Algorithms with Local
Search Chains (MA-LS-Chains)

	An implementation of an algorithm family for continuous
    optimization called memetic algorithms with local search chains
    (MA-LS-Chains), as proposed in Molina et al. (2010) <doi:10.1162/evco.2010.18.1.18102> and Molina et al. (2011) <doi:10.1007/s00500-010-0647-2>. Rmalschains is further discussed in Bergmeir et al. (2016) <doi:10.18637/jss.v075.i04>. Memetic algorithms are hybridizations of genetic
    algorithms with local search methods. They are especially suited
    for continuous optimization.
	"""
	
	cran = "Rmalschains" 

	version("0.2-10", md5="afd17cacd51cb869edccb9e44602767f")

	depends_on("r-rcpp", type=("build", "run"))
