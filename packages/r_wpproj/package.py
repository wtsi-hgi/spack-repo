# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWpproj(RPackage):
	"""Linear p-Wasserstein Projections

	Performs Wasserstein projections from the predictive distributions of any model into the space of predictive distributions of linear models. We utilize L1 penalties to also reduce the complexity of the model space. This package employs the methods as described in Dunipace, Eric and Lorenzo Trippa (2020) <arXiv:2012.09999>.
	"""
	
	homepage = "https://github.com/ericdunipace/WpProj"
	cran = "WpProj" 

	version("0.2.1", md5="ae3e3c9a5c3173d41853fe02bf088c3a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-oem", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-roi", type=("build", "run"))
	depends_on("r-roi-plugin-ecos", type=("build", "run"))
	depends_on("r-roi-plugin-lpsolve", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rqpen", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.4:", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcppcgal", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
