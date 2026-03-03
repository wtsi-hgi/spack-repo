# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffect(RPackage):
	"""Accelerated Functional Failure Time Model with
Error-Contaminated Survival Times

	We aim to deal with data with measurement error in the response and misclassification censoring status under an AFT model. This package primarily contains three functions, which are used to generate artificial data, correction for error-prone data and estimate the functional covariates for an AFT model.
	"""
	
	cran = "AFFECT" 

	version("0.1.2", md5="2156529938ef839be06c3e791a1dae59")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
