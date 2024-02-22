# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoogleerrorreportingr(RPackage):
	"""Send Error Reports to the Google Error Reporting Service API

	Send error reports to the Google Error Reporting service <https://cloud.google.com/error-reporting/> and view errors and assign error status in the Google Error Reporting user interface.
	"""
	
	homepage = "https://github.com/ixpantia/googleErrorReportingR"
	cran = "googleErrorReportingR" 

	version("0.0.4", md5="08dc8462f452353c2d500ea6c9b5b0fe")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
