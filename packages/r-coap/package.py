# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoap(RPackage):
	"""High-Dimensional Covariate-Augmented Overdispersed Poisson
Factor Model

	A covariate-augmented overdispersed Poisson factor model is proposed to jointly perform a high-dimensional Poisson factor analysis and estimate a large coefficient matrix for overdispersed count data.
    More details can be referred to Liu et al. (2024) <doi:10.48550/arXiv.2402.15071>.
	"""
	
	homepage = "https://github.com/feiyoung/COAP"
	cran = "COAP" 

	version("1.1", md5="6d3c7af047acca39c45f2ed5eb78d340")

	depends_on("r-irlba", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
