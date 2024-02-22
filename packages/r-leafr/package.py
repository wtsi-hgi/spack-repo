# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeafr(RPackage):
	"""Calculates the Leaf Area Index (LAD) and Other Related Functions

	A set of functions for analyzing the structure 
  of forests based on the leaf area density (LAD) and leaf area index (LAI) measures 
  calculated from Airborne Laser Scanning (ALS), i.e., scanning lidar (Light Detection 
  and Ranging) data. The methodology is discussed and described in 
  Almeida et al. (2019) <doi:10.3390/rs11010092> and 
  Stark et al. (2012) <doi:10.1111/j.1461-0248.2012.01864.x>.
	"""
	
	homepage = "https://github.com/DRAAlmeida/leafR"
	cran = "leafR" 

	version("0.3.5", md5="e6fec3b11a211bdcdad2e89643a9ffed")

	depends_on("r-lidr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
