# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbplyr(RPackage):
	"""A 'dplyr' Back End for Databases.

	A 'dplyr' back end for databases that allows you to work with remote
	database tables as if they are in-memory data frames. Basic features works
	with any database that has a 'DBI' back end; more advanced features require
	'SQL' translation to be provided by the package author."""

	cran = "dbplyr"

	license("MIT")

	version("2.4.0", md5="55d0e3258599d069e8d995b5d99b9a23")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-blob@1.2:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-dbi@1.1.3:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pillar@1.9:", type=("build", "run"))
	depends_on("r-purrr@1.0.1:", type=("build", "run"))
	depends_on("r-r6@2.2.2:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-vctrs@0.6.3:", type=("build", "run"))
	depends_on("r-withr@2.5:", type=("build", "run"))
