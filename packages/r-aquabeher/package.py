# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAquabeher(RPackage):
	"""Estimation of Rainy Season Calendar and Soil Water Balance for
Agriculture

	Computes and integrates daily reference 'evapotranspiration' ('Eto') into a water balance model, 
             to estimate the calendar of wet-season (Onset, Cessation and Duration) based on 'agroclimatic' 
             approach, for further information please refer to Allen 'et al.' (1998, ISBN:92-5-104219-5),
             Allen (2005, ISBN:9780784408056), 'Doorenbos' and Pruitt (1975, ISBN:9251002797)
             'Guo et al.' (2016) <doi:10.1016/j.envsoft.2015.12.019>, Hargreaves and 'Samani' (1985) 
             <doi:10.13031/2013.26773>, Priestley and Taylor (1972) <https://journals.ametsoc.org/downloadpdf/journals/mwre/100/2/1520-0493_1972_100_0081_otaosh_2_3_co_2.pdf>.
	"""
	
	homepage = "https://github.com/RobelTakele/AquaBEHER"
	cran = "AquaBEHER" 

	version("0.1.0", md5="f5789fae3eb70a37b0de15322afde9b9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
