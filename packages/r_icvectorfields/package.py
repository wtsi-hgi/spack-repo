# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcvectorfields(RPackage):
	"""Vector Fields from Spatial Time Series of Population Abundance

	Functions for converting time series of spatial abundance or density 
    data in raster format to vector fields of population movement using the digital 
    image correlation technique. More specifically, the functions in the package 
    compute cross-covariance using discrete fast Fourier transforms for computational 
    efficiency. Vectors in vector fields point in the direction of highest two 
    dimensional cross-covariance. The package has a novel implementation of the 
    digital image correlation algorithm that is designed to detect persistent 
    directional movement when image time series extend beyond a sequence of 
    two raster images. 
	"""
	
	cran = "ICvectorfields" 

	version("0.1.2", md5="01f593818bf1004af2ccce307dfea893")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fftwtools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-terra@1.5.21:", type=("build", "run"))
