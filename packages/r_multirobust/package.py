# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultirobust(RPackage):
	"""Multiply Robust Methods for Missing Data Problems

	Multiply robust estimation for population mean (Han and Wang 2013) <doi:10.1093/biomet/ass087>, regression analysis (Han 2014) <doi:10.1080/01621459.2014.880058> (Han 2016) <doi:10.1111/sjos.12177> and quantile regression (Han et al. 2019) <doi:10.1111/rssb.12309>.
	"""
	
	cran = "MultiRobust" 

	version("1.0.5", md5="4d472bf5d377bcb8e55ee55d8c1f7b0f")

