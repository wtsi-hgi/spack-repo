# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFjordlight(RPackage):
	"""Available Light Within the Water Column and Seafloor of Arctic
Fjords

	Satellite data collected between 2003 and 2022,
	in conjunction with gridded bathymetric data (50-150 m resolution),
	are used to estimate the irradiance reaching the bottom of a series of representative EU Arctic fjords. 
	An Earth System Science Data (ESSD) manuscript, Schlegel et al. (2023, in review), 
	that provides a detailed explanation of the methodology is currently in review.
	"""
	
	homepage = "https://github.com/FACE-IT-project/FjordLight"
	cran = "FjordLight" 

	version("0.7.0", md5="29ee37ebc489b09f0513f8d6555ebe44")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
