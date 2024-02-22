# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTulip(RPackage):
	"""A Toolbox for Linear Discriminant Analysis with Penalties

	Integrates several popular high-dimensional methods based on Linear Discriminant Analysis (LDA) and provides a comprehensive and user-friendly toolbox for linear, semi-parametric and tensor-variate classification as mentioned in Yuqing Pan, Qing Mai and Xin Zhang (2019) <arXiv:1904.03469>. Functions are included for covariate adjustment, model fitting, cross validation and prediction.
	"""
	
	cran = "TULIP" 

	version("1.0.2", md5="2c7e31eb03886adc4c476aa30c05bcf0")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-tensr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
