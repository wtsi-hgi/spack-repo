# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultikink(RPackage):
	"""Estimation and Inference for Multi-Kink Quantile Regression

	Estimation and inference for multiple kink quantile regression for longitudinal data and the i.i.d data. A bootstrap restarting iterative segmented quantile algorithm is proposed to estimate the multiple kink quantile regression model conditional on a given number of change points. The number of kinks is also allowed to be unknown. In such case, the backward elimination algorithm and the bootstrap restarting iterative segmented quantile algorithm are combined to select the number of change points based on a quantile BIC. For longitudinal data, we also develop the GEE estimator to incorporate the within-subject correlations.  A score-type based test statistic is also developed for testing the existence of kink effect. The package is based on the paper, ``Wei Zhong, Chuang Wan and Wenyang Zhang (2022). Estimation and inference for multikink quantile regression, JBES'' and ``Chuang Wan, Wei Zhong, Wenyang Zhang and Changliang Zou (2022). Multi-kink quantile regression for longitudinal data with application to progesterone data analysis, Biometrics". 
	"""
	
	cran = "MultiKink" 

	version("0.2.0", md5="45bdecd92c73eda021d485c2a53822a7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
