# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdcsis(RPackage):
	"""Conditional Distance Correlation Based Feature Screening and
Conditional Independence Inference

	Conditional distance correlation <doi:10.1080/01621459.2014.993081> is a novel conditional dependence measurement of two multivariate random variables given a confounding variable. This package provides conditional distance correlation, performs the conditional distance correlation sure independence screening procedure for ultrahigh dimensional data <http://www3.stat.sinica.edu.tw/statistica/J28N1/J28N114/J28N114.html>, and conducts conditional distance covariance test for conditional independence assumption of two multivariate variable.
	"""
	
	homepage = "https://github.com/Mamba413/cdcsis"
	cran = "cdcsis" 

	version("2.0.3", md5="38f8bfc0a09ad9b7dcbd90d274ea3a82")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-ks@1.8:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
