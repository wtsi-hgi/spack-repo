# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdwd(RPackage):
	"""Select and Download Climate Data from 'DWD' (German Weather
Service)

	Handle climate data from the 'DWD' ('Deutscher Wetterdienst', see 
             <https://www.dwd.de/EN/climate_environment/cdc/cdc_node_en.html> for more information).
             Choose observational time series from meteorological stations with 'selectDWD()'.
             Find raster data from radar and interpolation according to <https://bookdown.org/brry/rdwd/raster-data.html>.
             Download (multiple) data sets with progress bars and no re-downloads through 'dataDWD()'.
             Read both tabular observational data and binary gridded datasets with 'readDWD()'.
	"""
	
	homepage = "https://github.com/brry/rdwd"
	cran = "rdwd" 

	version("1.8.0", md5="9e13df2fd2138ca5a1754df5da308d0d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-berryfunctions@1.21.11:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
