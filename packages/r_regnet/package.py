# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegnet(RPackage):
	"""Network-Based Regularization for Generalized Linear Models

	Network-based regularization has achieved success in variable selection for 
    high-dimensional biological data due to its ability to incorporate correlations among 
    genomic features. This package provides procedures of network-based variable selection 
    for generalized linear models (Ren et al. (2017) <doi:10.1186/s12863-017-0495-5> and 
	Ren et al.(2019) <doi:10.1002/gepi.22194>). Continuous, binary, and survival response 
	are supported. Robust network-based methods are available for continuous and survival 
	responses. 
	"""
	
	homepage = "https://github.com/jrhub/regnet"
	cran = "regnet" 

	version("1.0.1", md5="c27436d3a3c06686cf7ffe1d5ae7a372")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
