# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErer(RPackage):
	"""Empirical Research in Economics with R

	Functions, datasets, and sample codes related to the book of 'Empirical Research in Economics: Growing up with R' by Dr. Changyou Sun are included. Marginal effects for binary or ordered choice models can be calculated. Static and dynamic Almost Ideal Demand System (AIDS) models can be estimated. A typical event analysis in finance can be conducted with several functions included.
	"""
	
	cran = "erer" 

	version("3.1", md5="aa98b62f6ce0c18c9d3af96403ff4c89")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-systemfit", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
