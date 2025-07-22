# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnvilbilling(RPackage):
	"""Provide functions to retrieve and report on usage expenses in NHGRI AnVIL (anvilproject.org).

	AnVILBilling helps monitor AnVIL-related costs in R, using queries to a BigQuery table to which costs are exported daily. Functions are defined to help categorize tasks and associated expenditures, and to visualize and explore expense profiles over time. This package will be expanded to help users estimate costs for specific task sets.
	"""
	
	bioc = "AnVILBilling"

	version("1.18.0", commit="4852ff774f91daef2b02a180c63ff1ea5acc81d0")
	version("1.12.0", commit="d93bfd5312ae161bd2e27fd023304944fbb3e35b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-bigrquery", type=("build", "run"))
	depends_on("r-shinytoastr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
