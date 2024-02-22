# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIheatmapr(RPackage):
	"""Interactive, Complex Heatmaps

	Make complex, interactive heatmaps. 'iheatmapr' includes a modular 
    system for iteratively building up complex heatmaps, as well as the 
    iheatmap() function for making relatively standard heatmaps.
	"""
	
	homepage = "https://docs.ropensci.org/iheatmapr/"
	cran = "iheatmapr" 

	version("0.7.1", md5="6a5cb805759d59d94769f25abe102a93")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
