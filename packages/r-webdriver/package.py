# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RWebdriver(RPackage):
	"""'WebDriver' Client for 'PhantomJS'

	A client for the 'WebDriver' 'API'. It allows driving a
    (probably headless) web browser, and can be used to test web
    applications, including 'Shiny' apps. In theory it works with any
    'WebDriver' implementation, but it was only tested with 'PhantomJS'.
	"""
	
	homepage = "https://github.com/rstudio/webdriver"
	cran = "webdriver" 

	version("1.0.6", md5="1e6bad48d7066af49789e08843ea875b")

	depends_on("r-callr@3.4.0:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-curl@2.0:", type=("build", "run"))
	depends_on("r-debugme", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-showimage", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
