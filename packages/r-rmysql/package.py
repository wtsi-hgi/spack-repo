# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmysql(RPackage):
	"""Database Interface and 'MySQL' Driver for R.

	Legacy 'DBI' interface to 'MySQL' / 'MariaDB' based on old code ported from
	S-PLUS. A modern 'MySQL' client based on 'Rcpp' is available  from the
	'RMariaDB' package."""

	cran = "RMySQL"

	version("0.10.27", md5="82055849b6008a804c59c5f1a9dafdaf")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-dbi@0.4:", type=("build", "run"))
	depends_on("mariadb-c-client", type=("build", "link", "run"))
