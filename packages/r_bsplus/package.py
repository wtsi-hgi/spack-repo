# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsplus(RPackage):
	"""Adds Functionality to the R Markdown + Shiny Bootstrap Framework

	The Bootstrap framework lets you add some JavaScript functionality to your web site by
  adding attributes to your HTML tags - Bootstrap takes care of the JavaScript
  <https://getbootstrap.com/docs/3.3/javascript/>. If you are using R Markdown or Shiny, you can
  use these functions to create collapsible sections, accordion panels, modals, tooltips,
  popovers, and an accordion sidebar framework (not described at Bootstrap site).
  Please note this package was designed for Bootstrap 3.3.
	"""
	
	homepage = "https://github.com/ijlyttle/bsplus"
	cran = "bsplus" 

	version("0.1.4", md5="45ebe222f507de689f560d7c497b3bbf")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
