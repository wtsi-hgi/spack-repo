# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSopie(RPackage):
	"""Non-Parametric Estimation of the Off-Pulse Interval of a Pulsar

	Provides functions to non-parametrically estimate the off-pulse interval of a source
    function originating from a pulsar. The technique is based on a sequential application of P-values
    obtained from goodness-of-fit tests for the uniform distribution, such as the Kolmogorov-Smirnov,
    Cramer-von Mises, Anderson-Darling and Rayleigh goodness-of-fit tests.
	"""
	
	cran = "SOPIE" 

	version("1.6", md5="759376f8b8957c8adbef36104945681c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-adgoftest", type=("build", "run"))
