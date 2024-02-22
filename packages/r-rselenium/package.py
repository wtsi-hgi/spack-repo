# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRselenium(RPackage):
	"""R Bindings for 'Selenium WebDriver'

	Provides a set of R bindings for the 'Selenium 2.0 WebDriver'
    (see <https://www.selenium.dev/documentation/>
    for more information) using the 'JsonWireProtocol' (see
    <https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol> for more
    information). 'Selenium 2.0 WebDriver' allows driving a web browser
    natively as a user would either locally or on a remote machine using
    the Selenium server it marks a leap forward in terms of web browser
    automation. Selenium automates web browsers (commonly referred to as
    browsers). Using RSelenium you can automate browsers locally or
    remotely.
	"""
	
	homepage = "https://docs.ropensci.org/RSelenium/"
	cran = "RSelenium" 

	version("1.7.9", md5="ed02ae9b7c70c299e1051d688ad5e3ed")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-wdman@0.2.2:", type=("build", "run"))
