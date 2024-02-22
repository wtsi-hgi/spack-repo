# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCropdemand(RPackage):
	"""Spatial Crop Water Demand for Brazil

	Estimation of crop water demand can be processed via this package. As example, the data  from 'TerraClimate' dataset (<https://www.climatologylab.org/terraclimate.html>) calibrated with automatic weather stations of National Meteorological Institute of Brazil is available in a coarse spatial resolution to do the crop water demand. However, the user have also the option to download the variables directly from 'TerraClimate' repository with the download.terraclimate function  and access the original 'TerraClimate' products. If the user believes that is necessary calibrate the variables, there is another function to do it. Lastly, the estimation of the crop water demand present in this package can be run for all the Brazilian territory with 'TerraClimate' dataset. 
	"""
	
	cran = "cropDemand" 

	version("1.0.3", md5="dfcbb1d200efe399f3004264be773050")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.3.0.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
