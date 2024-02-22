# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAides(RPackage):
	"""Additive Information & Details of Evidence Synthesis

	A supportive collection of functions for pooled analysis of aggregate data. The current version supports users to test assumptions before relevant analysis of bias from study size and sequential analysis such as mentioned by Wetterslev, J., Jakobsen, J. C., & Gluud, C. (2017) <doi:10.1186/s12874-017-0315-7>.  
	"""
	
	cran = "aides" 

	version("1.3.1", md5="8e08b120adeb7ceaa610301915d0492e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-meta", type=("build", "run"))
