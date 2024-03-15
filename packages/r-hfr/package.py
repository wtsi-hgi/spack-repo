# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHfr(RPackage):
	"""Estimate Hierarchical Feature Regression Models

	Provides functions for the estimation, plotting, predicting and cross-validation of hierarchical feature regression models as described in Pfitzinger (2024). Cluster Regularization via a Hierarchical Feature Regression. Econometrics and Statistics (in press). <doi:10.1016/j.ecosta.2024.01.003>.
	"""
	
	homepage = "https://hfr.residualmetrics.com"
	cran = "hfr" 

	version("0.7.1", md5="4819e54a6275ff43676f69c58ef715ff")

	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
