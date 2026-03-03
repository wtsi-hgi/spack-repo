# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistributionutils(RPackage):
	"""Distribution Utilities

	Utilities are provided which are of use in the
    packages I have developed for dealing with
    distributions. Currently these packages are GeneralizedHyperbolic,
    VarianceGamma, and SkewHyperbolic and NormalLaplace. Each of these
    packages requires DistributionUtils. Functionality includes sample
    skewness and kurtosis, log-histogram, tail plots, moments by
    integration, changing the point about which a moment is
    calculated, functions for testing distributions using inversion
    tests and the Massart inequality. Also includes an implementation
    of the incomplete Bessel K function.
	"""
	
	cran = "DistributionUtils" 

	version("0.6-1", md5="07fb4777b695b505d1dc0cfbc65209da")

	depends_on("r@3.0.1:", type=("build", "run"))
