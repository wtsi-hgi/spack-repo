# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMashr(RPackage):
	"""Multivariate Adaptive Shrinkage

	Implements the multivariate adaptive shrinkage (mash)
    method of Urbut et al (2019) <DOI:10.1038/s41588-018-0268-8> for
    estimating and testing large numbers of effects in many conditions
    (or many outcomes). Mash takes an empirical Bayes approach to
    testing and effect estimation; it estimates patterns of similarity
    among conditions, then exploits these patterns to improve accuracy
    of the effect estimates. The core linear algebra is implemented in
    C++ for fast model fitting and posterior computation.
	"""
	
	homepage = "https://github.com/stephenslab/mashr"
	cran = "mashr" 

	version("0.2.79", md5="3ddec828c72b1d1b594f35a3934e7f88")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ashr@2.2.22:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rmeta", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-softimpute", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppgsl@0.3.8:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
