# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcesat2r(RPackage):
	"""ICESat-2 Altimeter Data using R

	Programmatic connection to the 'OpenAltimetry API' <https://openaltimetry.org/data/swagger-ui/> to download and process 'ATL03' (Global Geolocated Photon Data), 'ATL06' (Land Ice Height), 'ATL07' (Sea Ice Height), 'ATL08' (Land and Vegetation Height), 'ATL10' (Sea Ice Freeboard), 'ATL12' (Ocean Surface Height) and 'ATL13' (Inland Water Surface Height) 'ICESat-2' Altimeter Data. The user has the option to download the data by selecting a bounding box from a 1- or 5-degree grid globally utilizing a shiny application. The 'ICESat-2' mission collects altimetry data of the Earth's surface. The sole instrument on 'ICESat-2' is the Advanced Topographic Laser Altimeter System (ATLAS) instrument that measures ice sheet elevation change and sea ice thickness, while also generating an estimate of global vegetation biomass. 'ICESat-2' continues the important observations of ice-sheet elevation change, sea-ice freeboard, and vegetation canopy height begun by 'ICESat' in 2003.
	"""
	
	homepage = "https://github.com/mlampros/IceSat2R"
	cran = "IceSat2R" 

	version("1.0.4", md5="1511261bfce345ae5501dabc1b9b57bd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-lwgeom", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-leafgl", type=("build", "run"))
	depends_on("r-leaflet-extras", type=("build", "run"))
	depends_on("r-leafsync", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("udunits@2:", type=("build", "link", "run"))
	depends_on("geos", type=("build", "link", "run"))
	depends_on("proj", type=("build", "link", "run"))
	depends_on("unzip", type=("build", "link", "run"))
