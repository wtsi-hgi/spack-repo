# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTggd(RPackage):
	"""The Standard Distribution Functions for the Truncated
Generalised Gamma Distribution

	Density, distribution function, quantile function and random generation for the Truncated Generalised Gamma Distribution (also in log10(x) and ln(x) space).
	"""
	
	cran = "tggd" 

	version("0.1.1", md5="c6329a5e967769914943f28726f43405")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
