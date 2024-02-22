# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarkovchain(RPackage):
	"""Easy Handling Discrete Time Markov Chains

	Functions and S4 methods to create and manage discrete time Markov
    chains more easily. In addition functions to perform statistical (fitting
    and drawing random variates) and probabilistic (analysis of their structural
    proprieties) analysis are provided. See Spedicato (2017) <doi:10.32614/RJ-2017-036>.
    Some functions for continuous times Markov chains depends on the suggested ctmcd package, that, 
    as May 2023, can be retrieved from <https://cran.r-project.org/src/contrib/Archive/ctmcd/ctmcd_1.4.2.tar.gz>.
	"""
	
	homepage = "https://github.com/spedygiorgio/markovchain/"
	cran = "markovchain" 

	version("0.9.5", md5="684f00bec56ebc23e97d0d9fbbafe4a1")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.600.4:", type=("build", "run"))
