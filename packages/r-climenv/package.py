# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimenv(RPackage):
	"""Download, Extract and Visualise Climate and Elevation Data

	Grants access to three widely recognised modelled data sets, namely
    Global Climate Data (WorldClim 2), Climatologies at high resolution for the
    earth's land surface areas (CHELSA), and National Aeronautics and Space
    Administration's (NASA) Shuttle Radar Topography Mission (SRTM). It handles
    both multi and single geospatial polygon and point data, extracts outputs
    that can serve as covariates in various ecological studies. Provides two
    common graphic options – the Walter-Lieth (1960)
    <https://donum.uliege.be/bitstream/2268.1/7079/1/Walter-Lieth_Klimadiagramm-Weltatlas.pdf> 
    climate diagram and the Holdridge (1967)
    <https://reddcr.go.cr/sites/default/files/centro-de-documentacion/holdridge_1966_-_life_zone_ecology.pdf>
    life zone classification scheme. Provides one new graphic scheme of our own
    design which incorporates aspects of both Walter-Leigh and Holdridge.
    Provides user-friendly access and extraction of globally recognisable data
    sets to enhance their usability across a broad spectrum of applications.
	"""
	
	homepage = "https://github.com/jamestsakalos/climenv"
	cran = "climenv" 

	version("1.0.0", md5="4798a7307711ee07542730404f7d66be")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-climaemet", type=("build", "run"))
	depends_on("r-dismo", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-elevatr@0.99:", type=("build", "run"))
	depends_on("r-exactextractr", type=("build", "run"))
	depends_on("r-geodata", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-ternary", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
