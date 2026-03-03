# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbtransmission(RPackage):
	"""Naive Bayes Transmission Analysis

	Estimates the relative transmission probabilities between cases in an infectious disease outbreak or cluster using naive Bayes. Included are various functions to use these probabilities to estimate transmission parameters such as the generation/serial interval and reproductive number as well as finding the contribution of covariates to the probabilities and visualizing results. The ideal use is for an infectious disease dataset with metadata on the majority of cases but more informative data such as contact tracing or pathogen whole genome sequencing on only a subset of cases. For a detailed description of the methods see Leavitt et al. (2020) <doi:10.1093/ije/dyaa031>.
	"""
	
	homepage = "https://sarahleavitt.github.io/nbTransmission/"
	cran = "nbTransmission" 

	version("1.1.4", md5="2c98986e65b8b0c20c3812af92a624bd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-poisbinom", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
