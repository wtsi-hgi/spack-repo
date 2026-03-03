# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAppestimation(RPackage):
	"""Adjusted Prediction Model Performance Estimation

	Calculating predictive model performance measures adjusted for predictor distributions using density ratio method (Sugiyama et al., (2012, ISBN:9781139035613)). L1 and L2 error for continuous outcome and C-statistics for binomial outcome are computed. 
	"""
	
	cran = "APPEstimation" 

	version("0.1.1", md5="a847fe71138950bb48e63d3287850c05")

	depends_on("r-densratio", type=("build", "run"))
