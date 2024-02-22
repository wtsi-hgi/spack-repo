# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPysparklyr(RPackage):
	"""Provides a 'PySpark' Back-End for the 'sparklyr' Package

	It enables 'sparklyr' to integrate with 'Spark Connect', and
    'Databricks Connect' by providing a wrapper over the 'PySpark' 'python'
    library.
	"""
	
	homepage = "https://github.com/mlverse/pysparklyr"
	cran = "pysparklyr" 

	version("0.1.3", md5="4c97acb92ff5dadaea11eb7083cb6517")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reticulate@1.33:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sparklyr@1.8.4:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-rsconnect", type=("build", "run"))
