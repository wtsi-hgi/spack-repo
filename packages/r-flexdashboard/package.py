# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexdashboard(RPackage):
	"""R Markdown Format for Flexible Dashboards

	Format for converting an R Markdown document to a grid
    oriented dashboard. The dashboard flexibly adapts the size of it's
    components to the containing web page.
	"""
	
	homepage = "https://pkgs.rstudio.com/flexdashboard/"
	cran = "flexdashboard" 

	version("0.6.2", md5="bf9c9236fc22c058cd4ca4eb8de0cb58")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-bslib@0.2.5:", type=("build", "run"))
	depends_on("r-htmltools@0.5.1:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.6:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr@1.30:", type=("build", "run"))
	depends_on("r-rmarkdown@2.8:", type=("build", "run"))
	depends_on("r-sass", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
