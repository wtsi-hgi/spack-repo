# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelenium(RPackage):
	"""Low-Level Browser Automation Interface

	An implementation of 'W3C WebDriver 2.0'
  (<https://w3c.github.io/webdriver/>), allowing interaction
  with a 'Selenium Server' (<https://www.selenium.dev/documentation/grid/>)
  instance from 'R'. Allows a web browser to be automated from 'R'.
	"""
	
	homepage = "https://ashbythorpe.github.io/selenium-r/"
	cran = "selenium" 

	version("0.1.3", md5="c6ff65dd3f86881de0f6febdcb5b5703")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
