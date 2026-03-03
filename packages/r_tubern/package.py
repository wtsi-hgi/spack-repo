# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTubern(RPackage):
	"""R Client for the YouTube Analytics and Reporting API

	Get statistics and reports from YouTube. To learn more about
    the YouTube Analytics and Reporting API, see <https://developers.google.com/youtube/reporting/>.
	"""
	
	homepage = "http://github.com/soodoku/tubern"
	cran = "tubern" 

	version("0.1.0", md5="6ab32653aa7426ecf8de7c73657aa7e0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
