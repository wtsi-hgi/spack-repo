# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCryptotrackr(RPackage):
	"""An Interface to Crypto Data Sources

	Allows you to connect to data sources across the 
        crypto ecosystem. This data can enable a range of activity such as 
        portfolio tracking, programmatic trading, or industry analysis.
	"""
	
	cran = "cryptotrackr" 

	version("1.1.0", md5="119c4ea8d310a025e2ed16de449d5b2a")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
