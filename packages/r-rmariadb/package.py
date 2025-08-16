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
	version("1.2.2", sha256="c97c61ace584f9ad9929d3e3f366556e0eecad12bc98ea2979563a01475f468e")
	version("1.2.1", sha256="c9176a096854ce33a98ce0faef0065c50b5d356174f90cea742c70e130cf5f0c")
	version("1.1.0", sha256="9ffa63a15052876a51a7996ca4e6a5b7b937f594b5cc7ca5a86f43789e22a956")
	version("1.0.8", sha256="3c8aedc519dc063ceb068535a3700bc5caf26f867078cc5a228aa8961e2d99f5")

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
		# The dependency is named 'mariadb-c-client' in Spack
		lib_dir = self.spec["mariadb-c-client"].prefix.lib.mariadb
		inc_dir = self.spec["mariadb-c-client"].prefix.include.mariadb
		args = ["LIB_DIR={0}".format(lib_dir), "INCLUDE_DIR={0}".format(inc_dir)]
		return args
