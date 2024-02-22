# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeonstore(RPackage):
	"""NEON Data Store

	The National Ecological Observatory Network (NEON) provides access
  to its numerous data products through its REST API, 
  <https://data.neonscience.org/data-api/>. This package provides a
  high-level user interface for downloading and storing NEON data products.
  Unlike 'neonUtilities', this package will avoid repeated downloading,
  provides persistent storage, and improves performance.  'neonstore' can also
  construct a local 'duckdb' database of stacked tables, making it possible
  to work with tables that are far to big to fit into memory.
	"""
	
	cran = "neonstore" 

	version("0.5.0", md5="030821c4019c8f8cd003883b06e14286")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-duckdb@0.2.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-thor", type=("build", "run"))
	depends_on("r-vroom@1.5.1:", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-duckdbfs", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
