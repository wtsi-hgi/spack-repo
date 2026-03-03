# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosaicmodel(RPackage):
	"""An Interface to Statistical Modeling Independent of Model
Architecture

	Provides functions for evaluating, displaying, and interpreting statistical models. The goal is to abstract the operations on models from the particular architecture of the model. For instance, calculating effect sizes rather than looking at coefficients. The package includes interfaces to both regression and classification architectures, including lm(), glm(), rlm() in 'MASS', random forests and recursive partitioning, k-nearest neighbors, linear and quadratic discriminant analysis, and models produced by the 'caret' package's train(). It's straightforward to add in other other model architectures.
	"""
	
	cran = "mosaicModel" 

	version("0.3.0", md5="ba73a2bf1d0715abe12536970067df65")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mosaiccore", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggformula", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
