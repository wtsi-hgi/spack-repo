# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarp(RPackage):
	"""Model-Averaged Renewal Process

	To implement a model-averaging approach with different renewal
    models, with a primary focus on forecasting large earthquakes. Based on
    six renewal models (i.e., Poisson, Gamma, Log-Logistics, Weibull,
    Log-Normal and BPT), model-averaged point estimates are calculated using
    AIC (or BIC) weights. Additionally, both percentile and studentized
    bootstrapped model-averaged confidence intervals are constructed. In
    comparison, point and interval estimation from the individual or "best"
    model (determined via model selection) can be retrieved. 
	"""
	
	homepage = "https://github.com/kanji709/marp"
	cran = "marp" 

	version("0.1.0", md5="d5aa223e9010269165a8f2370b91f2bb")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
