# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalgam(RPackage):
	"""Estimation of Causal Effects with Generalized Additive Models

	Implements various estimators for average
  treatment effects - an inverse probability weighted (IPW) estimator, 
  an augmented inverse probability weighted (AIPW) estimator, and a standard
  regression estimator - that make use of generalized additive models for
  the treatment assignment model and/or outcome model. See: Glynn, Adam N.
  and Kevin M. Quinn. 2010. "An Introduction to the Augmented Inverse
  Propensity Weighted Estimator." Political Analysis. 18: 36-56.
	"""
	
	cran = "CausalGAM" 

	version("0.1-4", md5="3f371d368cee7c108e416e2892bcaa6c")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-gam@1.0.1:", type=("build", "run"))
