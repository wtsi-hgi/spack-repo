# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeometa(RPackage):
	"""Tools for Reading and Writing ISO/OGC Geographic Metadata

	Provides facilities to handle reading and writing of geographic metadata 
 defined with OGC/ISO 19115, 11119 and 19110 geographic information metadata standards,
 and encoded using the ISO 19139 (XML) standard. It includes also a facility to check
 the validity of ISO 19139 XML encoded metadata.
	"""
	
	homepage = "https://github.com/eblondel/geometa/wiki"
	cran = "geometa" 

	version("0.7-1", md5="74e581d4e832dadac8ef2ec19c48a81d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
