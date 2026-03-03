# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpresto(RPackage):
	"""DBI Connector to Presto

	Implements a 'DBI' compliant interface to Presto. Presto is
    an open source distributed SQL query engine for running interactive
    analytic queries against data sources of all sizes ranging from
    gigabytes to petabytes: <https://prestodb.io/>.
	"""
	
	homepage = "https://github.com/prestodb/RPresto"
	cran = "RPresto" 

	version("1.4.6", md5="9311c5517cbc7d8d89df7c1b42535e4e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dbi@0.3:", type=("build", "run"))
	depends_on("r-httr@0.6:", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-dbplyr@2.3.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
