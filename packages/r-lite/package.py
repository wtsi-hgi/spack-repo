# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLite(RPackage):
	"""Likelihood-Based Inference for Time Series Extremes

	Performs likelihood-based inference for stationary time series 
    extremes.  The general approach follows Fawcett and Walshaw (2012)
    <doi:10.1002/env.2133>.  Marginal extreme value inferences are adjusted for 
    cluster dependence in the data using the methodology in Chandler and Bate 
    (2007) <doi:10.1093/biomet/asm015>, producing an adjusted log-likelihood 
    for the model parameters.  A log-likelihood for the extremal index is 
    produced using the K-gaps model of Suveges and Davison (2010) 
    <doi:10.1214/09-AOAS292>. These log-likelihoods are combined to make 
    inferences about extreme values. Both maximum likelihood and Bayesian 
    approaches are available.
	"""
	
	homepage = "https://paulnorthrop.github.io/lite/"
	cran = "lite" 

	version("1.1.0", md5="6dcf1df295a6663463b91556e091cfe2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-chandwich", type=("build", "run"))
	depends_on("r-exdex", type=("build", "run"))
	depends_on("r-revdbayes", type=("build", "run"))
	depends_on("r-rust", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
