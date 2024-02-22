# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiceconsnqp(RPackage):
	"""Symmetric Normalized Quadratic Profit Function

	Tools for econometric production analysis
   with the Symmetric Normalized Quadratic (SNQ) profit function,
   e.g. estimation, imposing convexity in prices,
   and calculating elasticities and shadow prices.
	"""
	
	homepage = "http://www.micEcon.org"
	cran = "micEconSNQP" 

	version("0.6-10", md5="57212eeb7c88becccae464ef3fe064f4")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-misctools@0.6.1:", type=("build", "run"))
	depends_on("r-systemfit@1.0.0:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
