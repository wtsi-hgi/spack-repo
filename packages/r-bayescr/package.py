# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayescr(RPackage):
	"""Bayesian Analysis of Censored Regression Models Under Scale
Mixture of Skew Normal Distributions

	Propose a parametric fit for censored linear regression models based on SMSN distributions, from a Bayesian perspective. Also, generates SMSN random variables.
	"""
	
	cran = "BayesCR" 

	version("2.1", md5="f69726e2e5a2026ddb14905a608771bf")

	depends_on("r@3.4.1:", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
