# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKisopenapi(RPackage):
	"""Korea Investment & Securities (KIS) Open Trading API

	API Wrapper to use Korea Investment & Securities (KIS) trading 
             system that provides various financial services like stock price 
             check, orders and balance check 
             <https://apiportal.koreainvestment.com/>.
	"""
	
	cran = "kisopenapi" 

	version("0.0.2", md5="52acc9c743ad4175c6dc2e6e75b4b573")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli@3.3:", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-httr2@0.2.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.8:", type=("build", "run"))
