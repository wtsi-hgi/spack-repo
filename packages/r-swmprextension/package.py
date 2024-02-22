# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwmprextension(RPackage):
	"""Functions for Analyzing and Plotting Estuary Monitoring Data

	Tools for performing routine analysis and plotting tasks with environmental
    data from the System Wide Monitoring Program of the National Estuarine
    Research Reserve System <https://cdmo.baruch.sc.edu/>. This package builds
    on the functionality of the 'SWMPr' package <https://cran.r-project.org/package=SWMPr>,
    which is used to retrieve and organize the data. The combined set of tools
    address common challenges associated with continuous time series data
    for environmental decision making, and are intended for use in annual reporting activities.
    References:
    Beck, Marcus W. (2016) <ISSN 2073-4859><https://journal.r-project.org/archive/2016-1/beck.pdf>
    Rudis, Bob (2014) <https://rud.is/b/2014/11/16/moving-the-earth-well-alaska-hawaii-with-r/>.
    United States Environmental Protection Agency (2015) <https://cfpub.epa.gov/si/si_public_record_Report.cfm?Lab=OWOW&dirEntryId=327030>.
	"""
	
	cran = "SWMPrExtension" 

	version("2.2.5.1", md5="01255c6b9a7b5745f112f0ab81524dba")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-swmpr", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-ggimage", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
