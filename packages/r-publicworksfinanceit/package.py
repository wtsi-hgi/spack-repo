# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPublicworksfinanceit(RPackage):
	"""Soil Defense Investments in Italy: Data Retrieval, Analysis,
Visualization

	Facilitates the retrieval and analysis of financial data related to public works in Italy, 
    focusing on soil defense investments. It extracts data from 'OpenCoesione', 'OpenBDAP', 
    and the 'ReNDiS' database, eliminating the need for direct access to these platforms.
    The package boasts a user-friendly design, featuring real time updates and a set of functions 
    tailored for data retrieval and visualization.
    See the webpages for further information
    <http://www.rendis.isprambiente.it/rendisweb/>,
    <https://opencoesione.gov.it/en/>, and    
    <https://bdap-opendata.rgs.mef.gov.it/>.
	"""
	
	cran = "PublicWorksFinanceIT" 

	version("0.1.0", md5="dfe211d33d98c5c689755c2d72910f62")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
