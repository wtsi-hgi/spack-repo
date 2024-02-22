# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNdjson(RPackage):
	"""Wicked-Fast Streaming 'JSON' ('ndjson') Reader

	Streaming 'JSON' ('ndjson') has one 'JSON' record per-line
        and many modern 'ndjson' files contain large numbers of records.
        These constructs may not be columnar in nature, but it is often
        useful to read in these files and "flatten" the structure out to
        enable working with the data in an R 'data.frame'-like context.
        Functions are provided that make it possible to read in plain
        'ndjson' files or compressed ('gz') 'ndjson' files and either
        validate the format of the records or create "flat" 'data.table'
        structures from them.
	"""
	
	homepage = "https://github.com/hrbrmstr/ndjson"
	cran = "ndjson" 

	version("0.9.0", md5="441efe2e343772953042b479c3a561d9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
