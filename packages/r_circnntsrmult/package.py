# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircnntsrmult(RPackage):
	"""Multivariate Circular Data using MNNTS Models

	A collection of utilities for the statistical analysis of multivariate circular data using distributions based on Multivariate Nonnegative Trigonometric Sums (MNNTS). The package includes functions for calculation of densities and distributions, for the estimation of parameters, and more.
	"""
	
	cran = "CircNNTSRmult" 

	version("0.1.0", md5="6833c2cfa13d7540dfbeb3905cf8c38a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-psychtools", type=("build", "run"))
	depends_on("r-circnntsr", type=("build", "run"))
