# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToastui(RPackage):
	"""Interactive Tables, Calendars and Charts for the Web

	Create interactive tables, calendars and charts with 'TOAST UI' <https://ui.toast.com/> libraries to
  integrate in 'shiny' applications or 'rmarkdown' 'HTML' documents.
	"""
	
	homepage = "https://dreamrs.github.io/toastui/"
	cran = "toastui" 

	version("0.3.3", md5="ff076c3c90f56a3ff70bb6303dd650e8")
	version("0.3.1", md5="26ef32e7902b823eef2f5dfabeb8e937")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-phosphoricons", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny@1.1:", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
