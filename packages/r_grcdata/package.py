# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrcdata(RPackage):
	"""Parameter Inference and Optimal Designs for Grouped and/or
Right-Censored Count Data

	We implement two main functions.
    The first function uses a given grouped and/or
    right-censored grouping scheme and empirical data to infer parameters,
    and implements chi-square goodness-of-fit tests.
    The second function searches for the global optimal grouping
    scheme of grouped and/or right-censored count responses in surveys.
	"""
	
	cran = "GRCdata" 

	version("1.0", md5="eea9f3da0d4d528dccf23d4958d19fa6")

	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
