# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinybusy(RPackage):
	"""Busy Indicators and Notifications for 'Shiny' Applications

	Add indicators (spinner, progress bar, gif) in your 'shiny'
  applications to show the user that the server is busy. And other tools to let
  your users know something is happening (send notifications, reports, ...).
	"""
	
	homepage = "https://github.com/dreamRs/shinybusy"
	cran = "shinybusy" 

	version("0.3.3", md5="2ffd3f845e336a2049a579e1674f81b3")
	version("0.3.2", md5="cf385f473c93ea5b64b36b9d6d59afe5")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
