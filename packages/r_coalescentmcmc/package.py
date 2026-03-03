# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoalescentmcmc(RPackage):
	"""MCMC Algorithms for the Coalescent

	Flexible framework for coalescent analyses in R. It includes a main function running the  MCMC algorithm, auxiliary functions for tree rearrangement, and some functions to compute population genetic parameters. Extended description can be found in Paradis (2020) <doi:10.1201/9780429466700>. For details on the MCMC algorithm, see Kuhner et al. (1995) <doi:10.1093/genetics/140.4.1421> and Drummond et al. (2002) <doi:10.1093/genetics/161.3.1307>.
	"""
	
	cran = "coalescentMCMC" 

	version("0.4-4", md5="23ca50b5d026e1c4edd00fe2e2e45b5c")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
