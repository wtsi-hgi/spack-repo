# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTableschemaR(RPackage):
	"""Table Schema 'Frictionless Data'

	Allows to work with 'Table Schema' (<https://specs.frictionlessdata.io/table-schema/>). 'Table Schema' is well suited for use cases around handling and validating tabular data in text formats such as 'csv', but its utility extends well beyond this core usage, towards a range of applications where data benefits from a portable schema format. The 'tableschema.r' package can load and validate any table schema descriptor, allow the creation and modification of descriptors, expose methods for reading and streaming data that conforms to a 'Table Schema' via the 'Tabular Data Resource' abstraction.
	"""
	
	homepage = "https://github.com/frictionlessdata/tableschema-r"
	cran = "tableschema.r" 

	version("1.1.2", md5="f420283b6c92389e55de058653097ee6")

	depends_on("r-config", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-jsonvalidate", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
