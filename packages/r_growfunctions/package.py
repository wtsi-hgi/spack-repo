# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrowfunctions(RPackage):
	"""Bayesian Non-Parametric Dependent Models for Time-Indexed
Functional Data

	Estimates a collection of time-indexed functions under
    either of Gaussian process (GP) or intrinsic Gaussian Markov
    random field (iGMRF) prior formulations where a Dirichlet process
    mixture allows sub-groupings of the functions to share the same
    covariance or precision parameters.  The GP and iGMRF formulations
    both support any number of additive covariance or precision terms,
    respectively, expressing either or both of multiple trend and
    seasonality.
	"""
	
	cran = "growfunctions" 

	version("0.16", md5="4c62abf374014d44318ea98da0c7b55a")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-rcpp@0.12.16:", type=("build", "run"))
	depends_on("r-spam@2.7.0:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-reshape2@1.2.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.8.400:", type=("build", "run"))
