# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraveltimer(RPackage):
	"""Interface to 'Travel Time' API

	'Travel Time' API <https://docs.traveltime.com/api/overview/introduction> helps users find locations by journey time rather than using ‘as the crow flies’ distance.
  Time-based searching gives users more opportunities for personalisation and delivers a more relevant search.
	"""
	
	homepage = "https://github.com/traveltime-dev/traveltime-sdk-r"
	cran = "traveltimeR" 

	version("1.1.4", md5="0194cf31bf59e65d2d27a442c77a93ce")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rprotobuf", type=("build", "run"))
