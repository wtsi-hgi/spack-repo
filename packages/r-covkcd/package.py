# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovkcd(RPackage):
	"""Covariance Estimation for Matrix Data with the Kronecker-Core
Decomposition

	Matrix-variate covariance estimation via the Kronecker-core decomposition. Computes the Kronecker and core covariance matrices corresponding to an arbitrary covariance matrix, and provides an empirical Bayes covariance estimator that adaptively shrinks towards the space of separable covariance matrices. For details, see Hoff, McCormack and Zhang (2022) <arXiv:2207.12484> "Core Shrinkage Covariance Estimation for Matrix-variate data".
	"""
	
	cran = "covKCD" 

	version("0.1", md5="8aea8d592905bd316c8b664a108b06ae")

