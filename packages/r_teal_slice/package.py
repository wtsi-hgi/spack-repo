# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTealSlice(RPackage):
	"""Filter Module for 'teal' Applications

	Data filtering module for 'teal' applications.  Allows for
    interactive filtering of data stored in 'data.frame' and
    'MultiAssayExperiment' objects. Also displays filtered and unfiltered
    observation counts.
	"""
	
	homepage = "https://insightsengineering.github.io/teal.slice/"
	cran = "teal.slice" 

	version("0.5.0", md5="dd84e2289e97dd6b4a30b292ba5cda16")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bslib@0.4:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.5:", type=("build", "run"))
	depends_on("r-htmltools@0.5.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-logger@0.2:", type=("build", "run"))
	depends_on("r-plotly@4.9.2.2:", type=("build", "run"))
	depends_on("r-r6@2.2:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinycssloaders@1:", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets@0.6.2:", type=("build", "run"))
	depends_on("r-teal-data@0.4:", type=("build", "run"))
	depends_on("r-teal-logger@0.1.1:", type=("build", "run"))
	depends_on("r-teal-widgets@0.4:", type=("build", "run"))
