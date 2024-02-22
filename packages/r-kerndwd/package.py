# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKerndwd(RPackage):
	"""Distance Weighted Discrimination (DWD) and Kernel Methods

	A novel implementation that solves the linear distance weighted discrimination and the kernel distance weighted discrimination. Reference: Wang and Zou (2018) <doi:10.1111/rssb.12244>.
	"""
	
	cran = "kerndwd" 

	version("2.0.3", md5="83802dc69f78d4bfcf11410839ca82c2")

