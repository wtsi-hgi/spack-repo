# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHkrbook(RPackage):
	"""Apps and Data for the Book "Introduction to Statistics"

	Functions, Shiny apps and data for the book "Introduction to Statistics" by
   Wolfgang Karl Härdle, Sigbert Klinke, and Bernd Rönz (2015) <doi:10.1007/978-3-319-17704-5>.
	"""
	
	cran = "HKRbook" 

	version("0.1.3", md5="53227d0c1e2bd96f9a83d0f29f6af81d")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinydashboardplus", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-highlight", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
