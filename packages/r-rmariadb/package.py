# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmariadb(RPackage):
	"""Database Interface and 'MariaDB' Driver.

	Implements a 'DBI'-compliant interface to 'MariaDB'
	(<https://mariadb.org/>) and 'MySQL' (<https://www.mysql.com/>)
	databases."""

	cran = "RMariaDB"

	version("1.3.1", md5="b8dc2132b67846e8c16d73d221f2acbf")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-blob", type=("build", "run"))
	depends_on("r-dbi@1.1.3:", type=("build", "run"))
	depends_on("r-hms@0.5:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("r-plogr", type=("build", "run"))
	depends_on("mariadb-c-client", type=("build", "link", "run"))

	# Set the library explicitly to prevent configure from finding a system
	# mysql-client
	def configure_vars(self):
		lib_dir = self.spec["mariadb-client"].prefix.lib.mariadb
		inc_dir = self.spec["mariadb-client"].prefix.include.mariadb
		args = ["LIB_DIR={0}".format(lib_dir), "INCLUDE_DIR={0}".format(inc_dir)]
		return args
