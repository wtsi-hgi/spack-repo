# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSarpSnowprofile(RPackage):
	"""Snow Profile Analysis for Snowpack and Avalanche Research

	Analysis and plotting tools for snow profile data produced from manual snowpack 
  observations and physical snowpack models. The functions in this package support snowpack 
  and avalanche research by reading various formats of data (including CAAML, SMET,
  generic csv, and outputs from the snow cover model SNOWPACK), manipulate the data, and 
  produce graphics such as stratigraphy and time series profiles. Package developed by 
  the Simon Fraser University Avalanche Research Program <http://www.avalancheresearch.ca>. 
  Graphics apply visualization concepts from Horton, Nowak, and Haegeli (2020, 
  <doi:10.5194/nhess-20-1557-2020>).
	"""
	
	homepage = "http://www.avalancheresearch.ca"
	cran = "sarp.snowprofile" 

	version("1.3.2", md5="be990de434bb61c32f205e20c2d2498f")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
