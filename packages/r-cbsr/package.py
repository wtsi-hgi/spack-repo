# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbsr(RPackage):
	"""Fits Cubic Bezier Spline Functions to Intertemporal and Risky
Choice Data

	Uses monotonically constrained Cubic Bezier Splines (CBS) to approximate latent utility functions in intertemporal choice and risky choice data. For more information, see Lee, Glaze, Bradlow, and Kable <doi:10.1007/s11336-020-09723-4>.
	"""
	
	cran = "CBSr" 

	version("1.0.5", md5="122709a69dbacd8f7d0db5586ef4f261")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjava@0.9.11:", type=("build", "run"))
	depends_on("r-nlcoptim@0.6:", type=("build", "run"))
	depends_on("openjdk@1.7:", type=("build", "link", "run"))
