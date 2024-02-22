# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimevis(RPackage):
	"""Create Interactive Timeline Visualizations in R

	Create rich and fully interactive timeline visualizations.
    Timelines can be included in Shiny apps or R markdown documents.
    'timevis' includes an extensive API to manipulate a timeline after creation,
    and supports getting data out of the visualization into R. Based on the
    'vis.js' Timeline JavaScript library.
	"""
	
	homepage = "https://github.com/daattali/timevis"
	cran = "timevis" 

	version("2.1.0", md5="cef36ed488cc31c914cf689380c85e15")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-htmltools@0.2.6:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.6:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
