# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedmod(RPackage):
	"""Pedigree Models

	Provides functions to estimate mixed probit models using, for 
    instance, pedigree data like in <doi:10.1002/sim.1603>. The models are also 
    commonly called liability threshold models. The approximation is 
    based on direct log marginal likelihood approximations like the randomized 
    Quasi-Monte Carlo suggested by <doi:10.1198/106186002394> with a similar 
    procedure to approximate the derivatives. The minimax tilting method 
    suggested by <doi:10.1111/rssb.12162> is also supported. Graph-based methods 
    are also provided that can be used to simplify pedigrees.
	"""
	
	homepage = "https://github.com/boennecd/pedmod"
	cran = "pedmod" 

	version("0.2.4", md5="bb168e998dcfba01e6ca0499b26c565a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-psqn", type=("build", "run"))
