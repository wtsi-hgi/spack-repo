# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFbms(RPackage):
	"""Flexible Bayesian Model Selection and Model Averaging

	Implements MJMCMC (mode jumping MCMC) described in Hubin and Storvik (2018) <doi:10.1016/j.csda.2018.05.020> and GMJMCMC (genetically modified MJMCMC) described in Hubin et al. (2021) <doi:10.1613/jair.1.13047> algorithms as well as the subsampling counterpart described in Lachmann et al. (2022) <doi:10.1016/j.ijar.2022.08.018> for flexible Bayesian model selection and model averaging.
	"""
	
	cran = "FBMS" 

	version("1.0", md5="4cb577368d7837e5d296251d0876ba09")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fastglm", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
