# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulticoap(RPackage):
	"""High-Dimensional Covariate-Augmented Overdispersed Multi-Study
Poisson Factor Model

	We introduce factor models designed to jointly analyze high-dimensional count data from multiple studies by extracting study-shared and specified factors. Our factor models account for heterogeneous noises and overdispersion among counts with augmented covariates. We propose an efficient and speedy variational estimation procedure for estimating model parameters, along with a novel criterion for selecting the optimal number of factors and the rank of regression coefficient matrix. More details can be referred to Liu et al. (2024) <doi:10.48550/arXiv.2402.15071>.
	"""
	
	homepage = "https://github.com/feiyoung/MultiCOAP"
	cran = "MultiCOAP" 

	version("1.1", md5="ec027c2b24db27650d1a14857640eb93")

	depends_on("r-irlba", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
