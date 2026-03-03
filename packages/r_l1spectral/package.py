# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RL1spectral(RPackage):
	"""An L1-Version of the Spectral Clustering

	Provides an l1-version of the spectral clustering algorithm devoted to robustly clustering highly perturbed graphs using l1-penalty. This algorithm is described with more details in the preprint C. Champion, M. Champion, M. Blazère, R. Burcelin and J.M. Loubes, "l1-spectral clustering algorithm: a spectral clustering method using l1-regularization" (2022).
	"""
	
	cran = "l1spectral" 

	version("0.99.6", md5="259b82fa31e2316045a6753ded0b64ca")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-aricode", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cvtools", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
