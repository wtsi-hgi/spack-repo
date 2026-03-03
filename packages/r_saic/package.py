# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaic(RPackage):
	"""Akaike Information Criterion for Sparse Estimation

	Computes the Akaike information criterion for the generalized linear models (logistic regression, Poisson regression, and Gaussian graphical models) estimated by the lasso. 
	"""
	
	homepage = "https://doi.org/10.1214/16-EJS1179"
	cran = "sAIC" 

	version("1.0.1", md5="b215f9d4ee5a035646090f1f2e5fbae1")

