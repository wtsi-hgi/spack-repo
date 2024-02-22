# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSirthresholded(RPackage):
	"""Sliced Inverse Regression with Thresholding

	Implements a thresholded version of the Sliced Inverse Regression method (Li, K. C. (1991) <doi:10.2307/2290563>), which allows to do variable selection.
	"""
	
	homepage = "https://clement-w.github.io/SIRthresholded/"
	cran = "SIRthresholded" 

	version("1.0.2", md5="18e3e6b63adfa711abd6fb1dfb0dc681")

	depends_on("r-strucchange", type=("build", "run"))
