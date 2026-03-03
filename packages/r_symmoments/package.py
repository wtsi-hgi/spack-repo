# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSymmoments(RPackage):
	"""Symbolic Central and Noncentral Moments of the Multivariate
Normal Distribution

	Symbolic central and non-central moments of the multivariate normal distribution. Computes a standard representation, LateX code, and values at specified mean and covariance matrices.
	"""
	
	cran = "symmoments" 

	version("1.2.1", md5="520d4aff78d753b48c0fda1cdffa7726")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-multipol", type=("build", "run"))
