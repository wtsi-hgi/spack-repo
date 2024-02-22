# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPamscapes(RPackage):
	"""Tools for Summarising and Analysing Soundscape Data

	A variety of tools relevant to the analysis
    of marine soundscape data. There are tools for downloading AIS (automatic identification system)
    data from Marine Cadastre <https://marinecadastre.gov/ais/>,
    connecting AIS data to GPS coordinates, plotting summaries of various soundscape
    measurements, and downloading relevant environmental variables (wind, swell height) from the
    National Center for Atmospheric Research data server <https://rda.ucar.edu/datasets/ds084.1/>.
    Most tools were developed to work well with output from 'Triton' software, but can be adapted
    to work with any similar measurements.
	"""
	
	cran = "PAMscapes" 

	version("0.5.3", md5="1269cce2a4bfe63c1fb9f75a3ac93cfc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-hoardr", type=("build", "run"))
	depends_on("r-pammisc", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-tdigest", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
