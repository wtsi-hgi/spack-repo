# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmsafops(RPackage):
	"""Tools for CM SAF NetCDF Data

	The Satellite Application Facility on Climate Monitoring (CM SAF) 
    is a ground segment of the European Organization for the Exploitation of 
    Meteorological Satellites (EUMETSAT) and one of EUMETSATs Satellite Application 
    Facilities. The CM SAF contributes to the sustainable monitoring of the climate 
    system by providing essential climate variables related to the energy and water 
    cycle of the atmosphere (<https://www.cmsaf.eu>). It is a joint cooperation of eight 
    National Meteorological and Hydrological Services.
    The 'cmsafops' R-package provides a collection of R-operators for the analysis and 
    manipulation of CM SAF NetCDF formatted data. Other CF conform NetCDF data with time, 
	longitude and latitude dimension should be applicable, but there is no guarantee for 
	an error-free application.
    CM SAF climate data records are provided for free via (<https://wui.cmsaf.eu/safira>).
    Detailed information and test data are provided on the CM SAF webpage 
    (<http://www.cmsaf.eu/R_toolbox>).
	"""
	
	homepage = "https://www.cmsaf.eu"
	cran = "cmsafops" 

	version("1.3.0", md5="423a9eb218b64aab81f58fa2893faf37")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-fields@10.3:", type=("build", "run"))
	depends_on("r-fnn@1.1:", type=("build", "run"))
	depends_on("r-ncdf4@1.17:", type=("build", "run"))
	depends_on("r-rainfarmr@0.1:", type=("build", "run"))
	depends_on("r-raster@3:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-trend", type=("build", "run"))
	depends_on("r-searchtrees", type=("build", "run"))
