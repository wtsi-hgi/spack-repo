# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmsafvis(RPackage):
	"""Tools to Visualize CM SAF NetCDF Data

	The Satellite Application Facility on Climate Monitoring (CM SAF) 
    is a ground segment of the European Organization for the Exploitation of 
    Meteorological Satellites (EUMETSAT) and one of EUMETSATs Satellite Application 
    Facilities. The CM SAF contributes to the sustainable monitoring of the climate 
    system by providing essential climate variables related to the energy and water 
    cycle of the atmosphere (<https://www.cmsaf.eu>). It is a joint cooperation of eight 
    National Meteorological and Hydrological Services.
    The 'cmsafvis' R-package provides a collection of R-operators for the analysis and
    visualization of CM SAF NetCDF data.
	CM SAF climate data records are provided for free via (<https://wui.cmsaf.eu/safira>).
    Detailed information and test data are provided on the CM SAF webpage 
    (<http://www.cmsaf.eu/R_toolbox>).
	"""
	
	cran = "cmsafvis" 

	version("1.2.3", md5="e9fd2158085deee0d8cea5f4e1c9a6e5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-cmsafops@1.2.1:", type=("build", "run"))
	depends_on("r-colorspace@1.4:", type=("build", "run"))
	depends_on("r-countrycode@1.1:", type=("build", "run"))
	depends_on("r-fields@10.3:", type=("build", "run"))
	depends_on("r-mapproj@1.2.7:", type=("build", "run"))
	depends_on("r-maps@3.3:", type=("build", "run"))
	depends_on("r-ncdf4@1.17:", type=("build", "run"))
	depends_on("r-png@0.1:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
	depends_on("r-raster@3:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-terra@1.7:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rastervis", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
