# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgsmtr(RPackage):
	"""Bayesian Group Sparse Multi-Task Regression

	Implementation of Bayesian multi-task regression models and was developed within the context of imaging genetics. The package can currently fit two models. The Bayesian group sparse multi-task regression model of Greenlaw et al. (2017)<doi:10.1093/bioinformatics/btx215> can be fit with implementation using Gibbs sampling. An extension of this model developed by Song, Ge et al. to accommodate both spatial correlation as well as correlation across brain hemispheres can also be fit using either mean-field variational Bayes or Gibbs sampling. The model can also be used more generally for multivariate (non-imaging) phenotypes with spatial correlation.
	"""
	
	cran = "bgsmtr" 

	version("0.7", md5="f51e604989df82ab123daa84ab62a41c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix@1.2.6:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.5:", type=("build", "run"))
	depends_on("r-matrixcalc@1.0.3:", type=("build", "run"))
	depends_on("r-misctools@0.6.22:", type=("build", "run"))
	depends_on("r-coda@0.18.1:", type=("build", "run"))
	depends_on("r-edison@1.1.1:", type=("build", "run"))
	depends_on("r-statmod@1.4.26:", type=("build", "run"))
	depends_on("r-sparsemvn@0.2:", type=("build", "run"))
	depends_on("r-inline@0.3.15:", type=("build", "run"))
	depends_on("r-laplacesdemon@16.1:", type=("build", "run"))
	depends_on("r-glmnet@2.0.13:", type=("build", "run"))
	depends_on("r-cholwishart@0.9.3:", type=("build", "run"))
	depends_on("r-mnormt@1.5.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12.14:", type=("build", "run"))
