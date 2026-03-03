# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModistools(RPackage):
	"""Interface to the 'MODIS Land Products Subsets' Web Services

	Programmatic interface to the Oak Ridge National Laboratories
    'MODIS Land Products Subsets' web services 
    (<https://modis.ornl.gov/data/modis_webservice.html>). Allows for easy
    downloads of 'MODIS' time series directly to your R workspace or
    your computer.
	"""
	
	homepage = "https://github.com/bluegreen-labs/MODISTools"
	cran = "MODISTools" 

	version("1.1.5", md5="984c0791bd10797e78d2d03e2e432f18")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
