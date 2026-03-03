# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkynet(RPackage):
	"""Generates Networks from BTS Data

	A flexible tool that allows generating bespoke
    air transport statistics for urban studies based on publicly available
    data from the Bureau of Transport Statistics (BTS) in the United States
    <https://www.transtats.bts.gov/databases.asp?Z1qr_VQ=E&Z1qr_Qr5p=N8vn6v10&f7owrp6_VQF=D>.
	"""
	
	homepage = "https://github.com/ropensci/skynet"
	cran = "skynet" 

	version("1.4.3", md5="fcd2c5daa8faa89b825a679b03b9bbd7")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
