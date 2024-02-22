# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgam(RPackage):
	"""Poisson-Gamma Additive Models

	This work is an extension of the state space model for Poisson count data, Poisson-Gamma model, towards a semiparametric specification. Just like the generalized additive models (GAM), cubic splines are used for covariate smoothing. The semiparametric models are fitted by an iterative process that combines maximization of likelihood and backfitting algorithm.
	"""
	
	cran = "pgam" 

	version("0.4.17", md5="f11c55bb5aae99607d143e6d5d0c6798")

	depends_on("r@3:", type=("build", "run"))
