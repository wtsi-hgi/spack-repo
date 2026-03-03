# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWfe(RPackage):
	"""Weighted Linear Fixed Effects Regression Models for Causal
Inference

	Provides a computationally efficient way of fitting
	     weighted linear fixed effects estimators for causal
	     inference with various weighting schemes. Weighted linear
	     fixed effects estimators can be used to estimate the
	     average treatment effects under different identification
	     strategies. This includes stratified randomized
	     experiments, matching and stratification for
	     observational studies, first differencing, and
	     difference-in-differences. The package implements methods
	     described in Imai and Kim (2017) "When should We Use
	     Linear Fixed Effects Regression Models for Causal
	     Inference with Longitudinal Data?", available at
	     <https://imai.fas.harvard.edu/research/FEmatch.html>.
	"""
	
	cran = "wfe" 

	version("1.9.1", md5="209e765d58a762870a3bd3e0f060cb63")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
