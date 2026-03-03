# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxbcv(RPackage):
	"""Bias-Corrected Sandwich Variance Estimators for Marginal Cox
Analysis of Cluster Randomized Trials

	The implementation of bias-corrected sandwich variance estimators for the analysis of cluster randomized trials with time-to-event outcomes using the marginal Cox model, proposed by Wang et al. (under review).
	"""
	
	cran = "CoxBcv" 

	version("0.0.1.0", md5="0132a4cc13182246f5880be025dd5f69")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
