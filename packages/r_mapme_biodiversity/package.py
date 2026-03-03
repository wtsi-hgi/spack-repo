# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapmeBiodiversity(RPackage):
	"""Efficient Monitoring of Global Biodiversity Portfolios

	Biodiversity areas, especially primary forest, serve a
    multitude of functions for local economy, regional functionality of
    the ecosystems as well as the global health of our planet. Recently,
    adverse changes in human land use practices and climatic responses to
    increased greenhouse gas emissions, put these biodiversity areas under
    a variety of different threats. The present package helps to analyse a
    number of biodiversity indicators based on freely available
    geographical datasets. It supports computational efficient routines
    that allow the analysis of potentially global biodiversity portfolios.
    The primary use case of the package is to support evidence based
    reporting of an organization's effort to protect biodiversity areas
    under threat and to identify regions were intervention is most duly
    needed.
	"""
	
	homepage = "https://mapme-initiative.github.io/mapme.biodiversity/index.html"
	cran = "mapme.biodiversity" 

	version("0.5.0", md5="8eba75d1b93ffabadf3ad69e20c3ed4a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("gdal@3.0.0:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))
