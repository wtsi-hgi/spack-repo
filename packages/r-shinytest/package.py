# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RShinytest(RPackage):
	"""Test Shiny Apps

	For automated testing of Shiny applications, using
    a headless browser, driven through 'WebDriver'.
	"""
	
	homepage = "https://github.com/rstudio/shinytest"
	cran = "shinytest" 

	version("1.5.3", md5="9a26cfa32fa6f5e8ff3281ec2b9b871b")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-callr@2.0.3:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-debugme", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-pingr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rematch", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi@0.8.0.9002:", type=("build", "run"))
	depends_on("r-shiny@1.3.2:", type=("build", "run"))
	depends_on("r-testthat@1.0.0:", type=("build", "run"))
	depends_on("r-webdriver@1.0.6:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
