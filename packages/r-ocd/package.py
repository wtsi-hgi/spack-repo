# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcd(RPackage):
	"""High-Dimensional Multiscale Online Changepoint Detection

	Implements the algorithm in Chen, Wang and Samworth (2020) <arxiv:2003.03668> for online detection of sudden mean changes in a sequence of high-dimensional observations. It also implements methods by Mei (2010) <doi:10.1093/biomet/asq010>, Xie and Siegmund (2013) <doi:10.1214/13-AOS1094> and Chan (2017) <doi:10.1214/17-AOS1546>.
	"""
	
	cran = "ocd" 

	version("1.1", md5="d0a9303553222c2af32bbd076a5007a5")

