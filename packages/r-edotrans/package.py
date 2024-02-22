# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdotrans(RPackage):
	"""Euclidean Distance-Optimized Data Transformation

	A data transformation method which takes into account the special property of scale non-invariance with a breakpoint at 1 of the Euclidean distance.
	"""
	
	cran = "EDOtrans" 

	version("0.2.2", md5="080d76e16e02f53feeead0767c665afb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abcanalysis", type=("build", "run"))
	depends_on("r-opgmmassessment", type=("build", "run"))
