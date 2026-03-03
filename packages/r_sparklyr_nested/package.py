# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparklyrNested(RPackage):
	"""A 'sparklyr' Extension for Nested Data

	A 'sparklyr' extension adding the capability to work easily with nested data.
	"""
	
	cran = "sparklyr.nested" 

	version("0.0.4", md5="db301f2bdc330e2e2828eb6042d2e28c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-sparklyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-listviewer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("spark@1.6:", type=("build", "link", "run"))
