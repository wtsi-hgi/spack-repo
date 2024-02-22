# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmberr(RPackage):
	"""'Amber' Electronic Data Capture Client

	'Amber' is a server application for capturing electronic data records.
    Rich forms are used to collect data. This 'Amber' client allows
    to perform data extraction for reporting or data transfer at persistent location
    purposes.
	"""
	
	homepage = "https://github.com/obiba/amberr/"
	cran = "amberr" 

	version("1.0.0", md5="a86c9b64198961e36678b0b20d7157ec")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
