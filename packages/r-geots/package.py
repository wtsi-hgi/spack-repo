# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeots(RPackage):
	"""Methods for Handling and Analyzing Time Series of Satellite
Images

	Provides functions and methods for: splitting large raster objects
             into smaller chunks, transferring images from a binary format into raster 
             layers, transferring raster layers into an 'RData' file, calculating the 
             maximum gap (amount of consecutive missing values) of a numeric vector, 
             and fitting harmonic regression models to periodic time series. The homoscedastic
             harmonic regression model is based on G. Roerink, M. Menenti and W. Verhoef (2000) <doi:10.1080/014311600209814>.
	"""
	
	cran = "geoTS" 

	version("0.1.8", md5="01b1a41b7e896063f78b130ff6bbeace")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster@2.9.5:", type=("build", "run"))
	depends_on("r-doparallel@1.0.14:", type=("build", "run"))
	depends_on("r-ff@2.2.14:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-robustbase@0.95.0:", type=("build", "run"))
	depends_on("r-sp@1.2.0:", type=("build", "run"))
