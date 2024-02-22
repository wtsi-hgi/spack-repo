# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatteacherassistant(RPackage):
	"""An App that Assists Intro Statistics Instructors with Data Sets

	Includes an interactive application designed to support
    educators in wide-ranging disciplines, with a particular focus on
    those teaching introductory statistical methods (descriptive and/or
    inferential) for data analysis. Users are able to randomly generate
    data, make new versions of existing data through common adjustments
    (e.g., add random normal noise and perform transformations), and check
    the suitability of the resulting data for statistical analyses.
	"""
	
	homepage = "https://github.com/ccasement/StatTeacherAssistant"
	cran = "StatTeacherAssistant" 

	version("0.0.1", md5="eb9d1896b13be15fd2ea0cf9f8c74a0c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-desctools@0.99.47:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-dt@0.19:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-plotly@4.10:", type=("build", "run"))
	depends_on("r-rhandsontable@0.3.8:", type=("build", "run"))
	depends_on("r-rio@0.5.27:", type=("build", "run"))
	depends_on("r-rmatio@0.16:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-shinyalert@2:", type=("build", "run"))
	depends_on("r-shinybs@0.61:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-sortable@0.4.6:", type=("build", "run"))
	depends_on("r-stringi@1.7.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-teachingapps@1.0.8:", type=("build", "run"))
	depends_on("r-tidyr@1.2.1:", type=("build", "run"))
