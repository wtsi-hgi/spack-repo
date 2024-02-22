# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrr(RPackage):
	"""Alternative Implementations of Base R Functions

	Alternative implementations of some base R functions, including sort, order, and match.  Functions are simplified but can be faster or have other advantages.
	"""
	
	cran = "grr" 

	version("0.9.5", md5="7e5bb79c5fe4533e0d2ac80485912dec")

	depends_on("r@3:", type=("build", "run"))
