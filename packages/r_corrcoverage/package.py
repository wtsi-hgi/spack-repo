# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrcoverage(RPackage):
	"""Correcting the Coverage of Credible Sets from Bayesian Genetic
Fine Mapping

	Using a computationally efficient method, the package can
    be used to find the corrected coverage estimate of a credible set 
    of putative causal variants from Bayesian genetic fine-mapping. 
    The package can also be used to obtain a corrected credible set
    if required; that is, the smallest set of variants required such 
    that the corrected coverage estimate of the resultant credible set is  
    within some user defined accuracy of the desired coverage.
    Maller et al. (2012) <doi:10.1038/ng.2435>,
    Wakefield (2009) <doi:10.1002/gepi.20359>,
    Fortune and Wallace (2018) <doi:10.1093/bioinformatics/bty898>.
	"""
	
	homepage = "https://annahutch.github.io/corrcoverage"
	cran = "corrcoverage" 

	version("1.2.1", md5="c2b6655bb17d5deb9c5d710cf85c2e94")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
