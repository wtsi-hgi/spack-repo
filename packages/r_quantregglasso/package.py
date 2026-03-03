# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantregglasso(RPackage):
	"""Adaptively Weighted Group Lasso for Semiparametric Quantile
Regression Models

	Implements an adaptively weighted group Lasso procedure for simultaneous variable selection and structure identification in varying
  coefficient quantile regression models and additive quantile regression models with ultra-high dimensional covariates. The methodology, grounded
  in a strong sparsity condition, establishes selection consistency under certain weight conditions. To address the challenge of tuning parameter 
  selection in practice, a BIC-type criterion named high-dimensional information criterion (HDIC) is proposed. The Lasso procedure, guided by
  HDIC-determined tuning parameters, maintains selection consistency. Theoretical findings are strongly supported by simulation studies.
  (Toshio Honda, Ching-Kang Ing, Wei-Ying Wu, 2019, <DOI:10.3150/18-BEJ1091>).
	"""
	
	homepage = "https://github.com/egpivo/SpatPCA"
	cran = "QuantRegGLasso" 

	version("1.0.0", md5="8ccd21afe2ef82109f9ab0dfec4316d1")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
