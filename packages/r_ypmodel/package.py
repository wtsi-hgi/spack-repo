# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYpmodel(RPackage):
	"""The Short-Term and Long-Term Hazard Ratio Model for Survival
Data

	Inference procedures accommodate a flexible range of hazard ratio patterns with a two-sample semi-parametric model. This model contains the proportional hazards model and the proportional odds model as sub-models, and accommodates non-proportional hazards situations to the extreme of having crossing hazards and crossing survivor functions. Overall, this package has four major functions: 1) the parameter estimation, namely short-term and long-term hazard ratio parameters; 2) 95 percent and 90 percent point-wise confidence intervals and simultaneous confidence bands for the hazard ratio function; 3) p-value of the adaptive weighted log-rank test; 4) p-values of two lack-of-fit tests for the model. See the included "read_me_first.pdf" for brief instructions. In this version (1.1), there is no need to sort the data before applying this package.
	"""
	
	cran = "YPmodel" 

	version("1.4", md5="92a0d02d1a23f10cdcb0a39be168f88b")

	depends_on("r@3.5:", type=("build", "run"))
