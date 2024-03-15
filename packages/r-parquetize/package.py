# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParquetize(RPackage):
	"""Convert Files to Parquet Format

	Collection of functions to get files in parquet format.
    Parquet is a columnar storage file format <https://parquet.apache.org/>. 
    The files to convert can be of several formats 
    ("csv", "RData", "rds", "RSQLite", 
    "json", "ndjson", "SAS", "SPSS"...).
	"""
	
	homepage = "https://ddotta.github.io/parquetize/"
	cran = "parquetize" 

	version("0.5.7", md5="a0d4732c365f3613c76910f1e76fd61f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-haven@2.4:", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
