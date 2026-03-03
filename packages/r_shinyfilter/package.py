# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyfilter(RPackage):
	"""Use Interdependent Filters on Table Columns in Shiny Apps

	Allows to connect 'selectizeInputs' widgets as filters to a 'reactable' table. 
  As known from spreadsheet applications, column filters are interdependent, so each 
  filter only shows the values that are really available at the moment based on 
  the current selection in other filters. Filter values currently not available 
  (and also those being available) can be shown via popovers or tooltips.
	"""
	
	homepage = "https://github.com/jsugarelli/shinyfilter/"
	cran = "shinyfilter" 

	version("0.1.1", md5="0ff45c3a209df66666c0e156ffcd4b77")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
