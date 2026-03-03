# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAimsir17(RPackage):
	"""Irish Weather Observing Stations Hourly Records for 2017

	Named after the Irish name for weather, this package contains 
    tidied data from the Irish Meteorological Service's hourly observations for 2017. 
    In all, the data sets include observations from 25 weather stations, and also
    latitude and longitude coordinates for each weather station. Now includes energy 
    generation data for Ireland and Northern Ireland (2017), including Wind Generation data.
	"""
	
	homepage = "https://github.com/JimDuggan/aimsir17"
	cran = "aimsir17" 

	version("0.0.2", md5="c630d97f2badfbcdf7db22ab0ade7824", url="https://cran.r-project.org/src/contrib/aimsir17_0.0.2.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
