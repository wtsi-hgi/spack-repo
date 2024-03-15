# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigrquerystorage(RPackage):
	"""An Interface to Google's 'BigQuery Storage' API

	Easily talk to Google's 'BigQuery Storage' API from R
    (<https://cloud.google.com/bigquery/docs/reference/storage/rpc>).
	"""
	
	homepage = "https://github.com/meztez/bigrquerystorage"
	cran = "bigrquerystorage" 

	version("1.0.0", md5="f9d70806e386e18cfea1ba86de943106")

	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-bigrquery", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("protobuf", type=("build", "link", "run"))
