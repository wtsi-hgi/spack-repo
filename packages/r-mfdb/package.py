# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfdb(RPackage):
	"""MareFrame DB Querying Library

	Creates and manages a PostgreSQL database suitable for storing fisheries data
             and aggregating ready for use within a Gadget <https://gadget-framework.github.io/gadget2/> model.
             See <https://mareframe.github.io/mfdb/> for more information.
	"""
	
	cran = "mfdb" 

	version("7.3-1", md5="5ec6d13e7abb4949efd1500708636382")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-logging@0.7.103:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-duckdb@0.2.5:", type=("build", "run"))
	depends_on("r-getpass@0.1.1:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-rpostgres@1.3:", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
