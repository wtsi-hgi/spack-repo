# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRenvlp(RPackage):
	"""Computing Envelope Estimators

	Provides a general routine, envMU, which allows  estimation of the M envelope of span(U) given root n consistent estimators of M and U. The routine envMU does not presume a model.  This package implements response envelopes,  partial response envelopes,  envelopes in the predictor space,  heteroscedastic envelopes,  simultaneous envelopes,  scaled response envelopes,  scaled envelopes in the predictor space,  groupwise envelopes, weighted envelopes,  envelopes in logistic regression, envelopes in Poisson regression envelopes in function-on-function linear regression, envelope-based Partial Partial Least Squares,  envelopes with non-constant error covariance, envelopes with t-distributed errors, reduced rank envelopes and reduced rank envelopes with non-constant error covariance. For each of these model-based routines the package provides inference tools including bootstrap, cross validation, estimation and prediction, hypothesis testing on coefficients are included except for weighted envelopes. Tools for selection of dimension include AIC, BIC and likelihood ratio testing.   Background is available at Cook, R. D., Forzani, L. and Su, Z. (2016) <doi:10.1016/j.jmva.2016.05.006>. Optimization is based on a clockwise coordinate descent algorithm.
	"""
	
	cran = "Renvlp" 

	version("3.4.5", md5="1e59e90d49008ddefdbd44d8cd59b632")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-orthogonalsplinebasis", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
