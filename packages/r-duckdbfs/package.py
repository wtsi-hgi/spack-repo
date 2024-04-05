# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDuckdbfs(RPackage):
	"""High Performance Remote File System, Database and 'Geospatial'
Access Using 'duckdb'

	Provides friendly wrappers for creating 'duckdb'-backed connections
  to tabular datasets ('csv', parquet, etc) on local or remote file systems.
  This mimics the behaviour of "open_dataset" in the 'arrow' package, 
  but in addition to 'S3' file system also generalizes to any list of 'http' URLs.
	"""
	
	homepage = "https://github.com/cboettig/duckdbfs"
	cran = "duckdbfs" 

	version("0.0.4", md5="30b4da920ef74b18f984ce4225d3faf8")
	version("0.0.3", md5="5e309df740c691dde152c44980570a49")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-duckdb@0.9.2:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
