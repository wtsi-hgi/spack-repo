# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGimms(RPackage):
	"""Download and Process GIMMS NDVI3g Data

	This is a set of functions to retrieve information about GIMMS
    NDVI3g files currently available online; download (and re-arrange, in the 
    case of NDVI3g.v0) the half-monthly data sets; import downloaded files from 
    ENVI binary (NDVI3g.v0) or NetCDF format (NDVI3g.v1) directly into R based 
    on the widespread 'raster' package; conduct quality control; and generate 
    monthly composites (e.g., maximum values) from the half-monthly input data. 
    As a special gimmick, a method is included to conveniently apply the 
    Mann-Kendall trend test upon 'Raster*' images, optionally featuring 
    trend-free pre-whitening to account for lag-1 autocorrelation.
	"""
	
	homepage = "https://github.com/environmentalinformatics-marburg/gimms"
	cran = "gimms" 

	version("1.2.2", md5="f037737d6b6e033178192c58a3c5f1f9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-kendall", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-zyp", type=("build", "run"))
