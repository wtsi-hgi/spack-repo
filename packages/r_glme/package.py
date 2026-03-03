# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlme(RPackage):
	"""Generalized Linear Mixed Effects Models

	Provides Generalized Inferences based on exact distributions and exact probability statements for mixed effect models, provided by such papers as Weerahandi and Yu (2020) <doi:10.1186/s40488-020-00105-w> under the widely used Compound Symmetric Covariance structure. The package returns the estimation of the coefficients in random and fixed part of the mixed models by generalized inference.
	"""
	
	cran = "glme" 

	version("0.1.0", md5="a0f4debe440bdc2f9cf2044445d8a5c7")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
