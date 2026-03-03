# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsaucelabs(RPackage):
	"""R Wrapper for 'SauceLabs' REST API

	Retrieve, update, delete job information from <https://saucelabs.com/>. Poll the 'SauceLabs' services
    current status and access supported platforms. Send and retrieve files from 'SauceLabs' and manage tunnels associated
    with 'SauceConnect'.
	"""
	
	homepage = "http://johndharrison.github.io/RSauceLabs/"
	cran = "RSauceLabs" 

	version("0.1.6", md5="9c9859c522468b9a260b0191cf98a810")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
