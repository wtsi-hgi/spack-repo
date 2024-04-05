# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScdb(RPackage):
	"""Easily Access and Maintain Time-Based Versioned Data
(Slowly-Changing-Dimension)

	A collection of functions that enable easy access and updating of a database of data over time.
             More specifically, the package facilitates type-2 history for data-warehouses and provides a number
             of Quality of life improvements for working on SQL databases with R.
             For reference see Ralph Kimball and Margy Ross (2013, ISBN 9781118530801).
	"""
	
	homepage = "https://github.com/ssi-dk/SCDB"
	cran = "SCDB" 

	version("0.4.0", md5="fd75d3b24b27f3ea5bce5cb5c59b0d22")
	version("0.3", md5="c4fab556fd03dee5f361c4ce9831640d")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dbplyr@2.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
