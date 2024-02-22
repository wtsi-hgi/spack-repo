# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsdr(RPackage):
	"""Tools Developed for Structured Sufficient Dimension Reduction
(sSDR)

	Performs structured OLS (sOLS) and structured SIR (sSIR).
	"""
	
	cran = "sSDR" 

	version("1.2.0", md5="ff3b92f9d9a3865891be8632d7e9b79a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
