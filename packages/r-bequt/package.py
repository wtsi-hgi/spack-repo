# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBequt(RPackage):
	"""Bayesian Estimation for Quantile Regression Mixed Models

	Using a Bayesian estimation procedure, this package fits linear quantile regression models such as linear quantile models, linear quantile mixed models, quantile regression joint models for time-to-event and longitudinal data. The estimation procedure is based on the asymmetric Laplace distribution and the 'JAGS' software is used to get posterior samples (Yang, Luo, DeSantis (2019) <doi:10.1177/0962280218784757>).
	"""
	
	cran = "BeQut" 

	version("0.1.0", md5="5b8224d762c4847db9acdbd7e4ddf297")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-jagsui", type=("build", "run"))
	depends_on("r-lqmm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("jags@4:", type=("build", "link", "run"))
