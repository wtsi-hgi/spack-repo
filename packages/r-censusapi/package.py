# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCensusapi(RPackage):
	"""Retrieve Data from the Census APIs

	A wrapper for the U.S. Census Bureau APIs that returns data frames of 
	Census data and metadata. Available datasets include the 
	Decennial Census, American Community Survey, Small Area Health Insurance Estimates,
	Small Area Income and Poverty Estimates, Population Estimates and Projections, and more.
	"""
	
	homepage = "https://www.hrecht.com/censusapi/"
	cran = "censusapi" 

	version("0.8.0", md5="051302af77fe69fba3021d00f191023a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
