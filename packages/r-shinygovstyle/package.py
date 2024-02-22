# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinygovstyle(RPackage):
	"""Custom Gov Style Inputs for Shiny

	Collection of 'shiny' application styling that are the based on 
  the GOV.UK Design System.  See 
  <https://design-system.service.gov.uk/components/> for details.
	"""
	
	homepage = "https://github.com/moj-analytical-services/shinyGovstyle"
	cran = "shinyGovstyle" 

	version("0.0.8", md5="cf8ad70277211721ff9333483a1e6099")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-shiny@0.14:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
