# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRzabbix(RPackage):
	"""R Module for Working with the 'Zabbix API'

	R interface to the 'Zabbix API' data <https://www.zabbix.com/documentation/3.0/manual/api/reference>. Enables easy and direct communication with 'Zabbix API' from 'R'.
	"""
	
	cran = "RZabbix" 

	version("0.1.0", md5="27251300e21814d7085698eeefeb606c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr@1.1:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.19:", type=("build", "run"))
