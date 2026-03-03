# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRclickhouse(RPackage):
	"""'Yandex Clickhouse' Interface for R with Basic 'dplyr' Support

	'Yandex Clickhouse' (<https://clickhouse.com/>) is a high-performance relational column-store database to enable
    big data exploration and 'analytics' scaling to petabytes of data. Methods are
    provided that enable working with 'Yandex Clickhouse' databases via
    'DBI' methods and using 'dplyr'/'dbplyr' idioms.
	"""
	
	homepage = "https://github.com/IMSMWU/RClickhouse"
	cran = "RClickhouse" 

	version("0.6.9", md5="d3a631226bf08c5cdf54f9b9e2efeca1")

	depends_on("r@3.6.2:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-dbplyr@2:", type=("build", "run"))
	depends_on("r-dbi@1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
