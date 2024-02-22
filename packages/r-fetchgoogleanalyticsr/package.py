# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFetchgoogleanalyticsr(RPackage):
	"""Get Data from Google Analytics via the 'Windsor.ai' API

	Collect  your data on digital marketing campaigns from Google Analytics using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "fetchGoogleAnalyticsR" 

	version("0.1.0", md5="7274b5acefc5343282c0776f08abd63a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
