# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQut(RPackage):
	"""Quantile Universal Threshold

	Thresholding based tests for null hypothesis of the form A beta =c, and the Quantile Universal Threshold (QUT) for lasso regularization of Generalized Linear Models (GLM) and square-root lasso to obtain a sparse model with a good compromise between high true positive rate and low false discovery rate. Giacobino et al. (2017) <doi:10.1214/17-EJS1366>. Sardy et al. (2017) <arXiv:1708.02908>.
	"""
	
	cran = "qut" 

	version("2.2", md5="8c1dff6849bf9019a007c566ed63cf8f")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-flare", type=("build", "run"))
