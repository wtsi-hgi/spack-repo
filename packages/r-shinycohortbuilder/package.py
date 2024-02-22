# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinycohortbuilder(RPackage):
	"""Modular Cohort-Building Framework for Analytical Dashboards

	You can easily add advanced cohort-building component
    to your analytical dashboard or simple 'Shiny' app.
    Then you can instantly start building cohorts using multiple
    filters of different types, filtering datasets, and filtering steps.
    Filters can be complex and data-specific, and together
    with multiple filtering steps you can use complex filtering rules.
    The cohort-building sidebar panel allows you to easily
    work with filters, add and remove filtering steps.
    It helps you with handling missing values during filtering,
    and provides instant filtering feedback with filter feedback plots.
    The GUI panel is not only compatible with native shiny
    bookmarking, but also provides reproducible R code.
	"""
	
	cran = "shinyCohortBuilder" 

	version("0.2.1", md5="80fa77898303ad4efa0a51b365d0da43")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggiraph", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny@1.7:", type=("build", "run"))
	depends_on("r-shinywidgets@0.7:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cohortbuilder@0.2:", type=("build", "run"))
	depends_on("r-trycatchlog", type=("build", "run"))
	depends_on("r-highr", type=("build", "run"))
	depends_on("r-shinygizmo@0.4.2:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
