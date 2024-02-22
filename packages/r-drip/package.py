# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrip(RPackage):
	"""Discontinuous Regression and Image Processing

	A collection of functions that perform jump regression
	     and image analysis such as denoising, deblurring and
	     jump detection.
	"""
	
	cran = "DRIP" 

	version("1.9", md5="cd871bdbf16637c50e04135b2cf3a505")

	depends_on("r@3.5:", type=("build", "run"))
