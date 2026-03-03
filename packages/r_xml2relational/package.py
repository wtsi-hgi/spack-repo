# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXml2relational(RPackage):
	"""Converting XML Documents into Relational Data Models

	Import an XML document with nested object structures and convert
    it into a relational data model. The result is a set of R dataframes 
    with foreign key relationships. The data model and the data can be exported as
    SQL code of different SQL flavors.
	"""
	
	homepage = "https://github.com/jsugarelli/xml2relational/"
	cran = "xml2relational" 

	version("0.1.1", md5="c7bd197f2c4513fbd7ef9a64af81abbf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
