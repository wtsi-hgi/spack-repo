# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXesreadr(RPackage):
	"""Read and Write XES Files

	Read and write XES Files to create event log objects used by the 'bupaR' framework. XES (Extensible Event Stream) is the `IEEE` standard for storing and sharing event data (see <http://standards.ieee.org/findstds/standard/1849-2016.html> for more info).
	"""
	
	homepage = "http://www.bupar.net"
	cran = "xesreadR" 

	version("0.2.3", md5="1bfc4353b7e3437709d25e4c29078fbc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-bupar", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
