# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVosondash(RPackage):
	"""User Interface for Collecting and Analysing Social Networks

	A 'Shiny' application for the interactive visualisation and
    analysis of networks that also provides a web interface for collecting
    social media data using 'vosonSML'.
	"""
	
	homepage = "https://github.com/vosonlab/VOSONDash"
	cran = "VOSONDash" 

	version("0.5.7", md5="05e9c18cb8d9f7b820784ab08b7d3ad6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-igraph@1.2.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-shiny@1.3.2:", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-systemfonts", type=("build", "run"))
	depends_on("r-syuzhet", type=("build", "run"))
	depends_on("r-textutils", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-vosonsml@0.29:", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
