# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpcp(RPackage):
	"""Some Nonparametric CUSUM Tests for Change-Point Detection in
Possibly Multivariate Observations

	Provides nonparametric CUSUM tests for detecting changes
  in possibly serially dependent univariate or low-dimensional
  multivariate observations. Retrospective tests sensitive to changes
  in the expectation, the variance, the covariance, the
  autocovariance, the distribution function, Spearman's rho, Kendall's
  tau, Gini's mean difference, and the copula are provided, as well as
  a test for detecting changes in the distribution of independent
  block maxima (with environmental studies in mind). The package also
  contains a test sensitive to changes in the autocopula and a
  combined test of stationarity sensitive to changes in the
  distribution function and the autocopula. The latest additions are
  an open-end sequential test based on the retrospective CUSUM
  statistic that can be used for monitoring changes in the mean of
  possibly serially dependent univariate observations, as well as
  closed-end and open-end sequential tests based on empirical
  distribution functions that can be used for monitoring changes in
  the contemporary distribution of possibly serially dependent
  univariate or low-dimensional multivariate observations.
	"""
	
	cran = "npcp" 

	version("0.2-5", md5="96569328ca46155ed0911d33f1c7c3fb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
