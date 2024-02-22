# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsereg(RPackage):
	"""Sparse Bayesian Models for Regression, Subgroup Analysis, and
Panel Data

	Sparse modeling provides a mean selecting a small number of non-zero effects from a large possible number of candidate effects.  This package includes a suite of methods for sparse modeling: estimation via EM or MCMC, approximate confidence intervals with nominal coverage, and diagnostic and summary plots.  The method can implement sparse linear regression and sparse probit regression.  Beyond regression analyses, applications include subgroup analysis, particularly for conjoint experiments, and panel data. Future versions will include extensions to  models with truncated outcomes, propensity score, and instrumental variable analysis.
	"""
	
	cran = "sparsereg" 

	version("1.2", md5="f1012693351ab1e4b345e9c7b185efe3")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
