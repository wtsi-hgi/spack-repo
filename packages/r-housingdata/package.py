# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHousingdata(RPackage):
	"""U.S. Housing Data from 2008 to 2016

	Monthly median home listing, sale price per square foot, and number of units sold for 2984 counties in the contiguous United States From 2008 to January 2016.  Additional data sets containing geographical information and links to Wikipedia are also included.
	"""
	
	homepage = "http://github.com/hafen/housingData"
	cran = "housingData" 

	version("0.3.0", md5="240142a67d28e2f212b944d767190fcb")

	depends_on("r@2.15:", type=("build", "run"))
