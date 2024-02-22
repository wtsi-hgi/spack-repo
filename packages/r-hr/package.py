# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHr(RPackage):
	"""Toolkit for Data Analytics in Human Resources

	Transform and analyze workforce data in meaningful ways for human resources (HR) analytics. Get started with workforce planning using a simple Shiny app.
	"""
	
	cran = "hR" 

	version("0.2.50", md5="8dd3078589984fab0726cac52aaee4bb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
