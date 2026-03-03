# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobmixglm(RPackage):
	"""Robust Generalized Linear Models (GLM) using Mixtures

	Robust generalized linear models (GLM) using a mixture method, as described in Beath (2018) <doi:10.1080/02664763.2017.1414164>. This assumes that the data are a mixture of standard observations, being a generalised linear model, and outlier observations from an overdispersed generalized linear model. The overdispersed linear model is obtained by including a normally distributed random effect in the linear predictor of the generalized linear model.
	"""
	
	cran = "robmixglm" 

	version("1.2-3", md5="373c367ddf47043ac9bea88fb0216c31")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-fastghquad", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
