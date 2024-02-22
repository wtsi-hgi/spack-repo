# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStempcens(RPackage):
	"""Spatio-Temporal Estimation and Prediction for Censored/Missing
Responses

	It estimates the parameters of a censored or missing data in spatio-temporal models using the SAEM algorithm (Delyon et al., 1999). This algorithm is a stochastic approximation of the widely used EM algorithm and an important tool for models in which the E-step does not have an analytic form. Besides the expressions obtained to estimate the parameters to the proposed model, we include the calculations for the observed information matrix using the method developed by Louis (1982). To examine the performance of the fitted model, case-deletion measure are provided.
	"""
	
	cran = "StempCens" 

	version("1.1.0", md5="ea42d0f837a7d34eff1970190658b7da")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-mcmcglmm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-distances", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
