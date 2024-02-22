# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHbsae(RPackage):
	"""Hierarchical Bayesian Small Area Estimation

	Functions to compute small area estimates based on a basic area or
    unit-level model. The model is fit using restricted maximum likelihood, or
    in a hierarchical Bayesian way. In the latter case numerical integration is
    used to average over the posterior density for the between-area variance.
    The output includes the model fit, small area estimates and corresponding
    mean squared errors, as well as some model selection measures. Additional functions
    provide means to compute aggregate estimates and mean squared errors, to minimally
    adjust the small area estimates to benchmarks at a higher aggregation
    level, and to graphically compare different sets of small area estimates.
	"""
	
	cran = "hbsae" 

	version("1.2", md5="01c77d2935e8142fdfb465c2f2f1d176")

	depends_on("r@2.15.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
