# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModgetxl(RPackage):
	"""A 'shiny' Module for Reading Excel Sheets

	This is a shiny module that presents a file picker user interface to get an Excel file name, and reads the Excel sheets using 'readxl' package and returns the resulting sheet(s) as a vector and data in dataframe(s).
	"""
	
	cran = "modgetxl" 

	version("0.4", md5="b8cb3eb2e0f43416a9f616be28439c63")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
