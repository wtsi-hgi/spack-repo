# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbasex(RPackage):
	"""'BaseX' Client

	'BaseX' <https://basex.org> is a XML database engine and a compliant 'XQuery 3.1' processor with full support of 'W3C Update Facility'. This package is a full client-implementation of the client/server protocol for 'BaseX' and provides functionalities to create, manipulate and query on XML-data. 
	"""
	
	homepage = "https://github.com/BenEngbers/RBaseX"
	cran = "RBaseX" 

	version("1.1.2", md5="afcb784aafb41e730e09c9beb9a5516b")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-pingr", type=("build", "run"))
	depends_on("r-rex", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
