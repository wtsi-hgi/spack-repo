# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmsaf(RPackage):
	"""A Toolbox for CM SAF NetCDF Data

	The Satellite Application Facility on Climate Monitoring (CM SAF) 
    is a ground segment of the European Organization for the Exploitation of 
    Meteorological Satellites (EUMETSAT) and one of EUMETSATs Satellite Application 
    Facilities. The CM SAF contributes to the sustainable monitoring of the climate 
    system by providing essential climate variables related to the energy and water 
    cycle of the atmosphere (<https://www.cmsaf.eu>). It is a joint cooperation of eight 
    National Meteorological and Hydrological Services.
    The 'cmsaf' R-package includes a 'shiny' based interface for an easy application of 
    the 'cmsafops' and 'cmsafvis' packages - the CM SAF R Toolbox. The Toolbox offers an 
    easy way to prepare, manipulate, analyse and visualize CM SAF NetCDF formatted data. 
    Other CF conform NetCDF data with time, longitude and latitude dimension should be 
    applicable, but there is no guarantee for an error-free application.
    CM SAF climate data records are provided for free via (<https://wui.cmsaf.eu/safira>).
    Detailed information and test data are provided on the CM SAF webpage 
    (<http://www.cmsaf.eu/R_toolbox>).
	"""
	
	homepage = "https://www.cmsaf.eu"
	cran = "cmsaf" 

	version("3.5.0", md5="2e352399fb977ee3fd3dd7726688b345")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cmsafops@1.2:", type=("build", "run"))
	depends_on("r-cmsafvis@1.1.5:", type=("build", "run"))
	depends_on("r-colourpicker@1:", type=("build", "run"))
	depends_on("r-colorspace@1.4:", type=("build", "run"))
	depends_on("r-fnn@1.1:", type=("build", "run"))
	depends_on("r-maps@3.3:", type=("build", "run"))
	depends_on("r-ncdf4@1.17:", type=("build", "run"))
	depends_on("r-r-utils@2.9:", type=("build", "run"))
	depends_on("r-raster@3:", type=("build", "run"))
	depends_on("r-shiny@1.4:", type=("build", "run"))
	depends_on("r-shinyfiles@0.8:", type=("build", "run"))
	depends_on("r-shinyjs@1.1:", type=("build", "run"))
	depends_on("r-shinythemes@1.1:", type=("build", "run"))
	depends_on("r-shinywidgets@0.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-searchtrees", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
