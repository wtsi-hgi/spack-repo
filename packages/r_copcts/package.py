# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopcts(RPackage):
	"""Copula-Based Semiparametric Analysis for Time Series Data with
Detection Limits

	Semiparametric estimation for censored time series
    with lower detection limit. The latent response is a sequence of
    stationary process with Markov property
    of order one.
    Estimation of copula parameter(COPC) and Conditional quantile estimation
    are included for five available copula functions.
    Copula selection methods based on L2 distance from empirical copula function
    are also included.
	"""
	
	cran = "CopCTS" 

	version("1.0.0", md5="0d6453f738aaf4783d80167fb0d26aef")

	depends_on("r-copula", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-copbasic", type=("build", "run"))
