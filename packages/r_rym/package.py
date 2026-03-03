# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRym(RPackage):
	"""R Interface to Yandex Metrica API

	Allows work with 'Management API' for load counters, segments, filters,
	user permissions and goals list from Yandex Metrica, 'Reporting API' allows you to get 
	information about the statistics of site visits and other data without
	using the web interface, 'Logs API' allows to receive non-aggregated data and 
	'Compatible with Google Analytics Core Reporting API v3' allows 
	receive information about site traffic and other data using field names 
	from Google Analytics Core API.	For more information see official 
	documents <https://yandex.ru/dev/metrika/doc/api2/concept/about-docpage>.
	"""
	
	homepage = "https://selesnow.github.io/rym/"
	cran = "rym" 

	version("1.0.6", md5="9700ccc7e8c4af61ae4d21d32e6b76db")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
