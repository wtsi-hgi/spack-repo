# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHttping(RPackage):
	"""'Ping' 'URLs' to Time 'Requests'

	A suite of functions to ping 'URLs' and to time
    'HTTP' 'requests'. Designed to work with 'httr'.
	"""
	
	homepage = "https://github.com/sckott/httping"
	cran = "httping" 

	version("0.2.0", md5="ab56e4e3b34f10034cde7ac77a39fd8c")

	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-pryr@0.1.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httpcode@0.2:", type=("build", "run"))
