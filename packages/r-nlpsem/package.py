# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlpsem(RPackage):
	"""Linear and Nonlinear Longitudinal Process in Structural Equation
Modeling Framework

	Provides computational tools for nonlinear longitudinal models, in particular the intrinsically nonlinear models, in four scenarios: (1) univariate longitudinal processes with growth factors, with or without covariates including time-invariant covariates (TICs) and time-varying covariates (TVCs); (2) multivariate longitudinal processes that facilitate the assessment of correlation or causation between multiple longitudinal variables; (3) multiple-group models for scenarios (1) and (2) to evaluate differences among manifested groups, and (4) longitudinal mixture models for scenarios (1) and (2), with an assumption that trajectories are from multiple latent classes. The methods implemented are introduced in Jin Liu (2023) <arXiv:2302.03237v2>.
	"""
	
	homepage = "https://github.com/Veronica0206/nlpsem"
	cran = "nlpsem" 

	version("0.3", md5="c1e6d47a8e2332d71c1da8bb69508043")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-openmx@2.21.8:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
