# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModeldb(RPackage):
	"""Fits Models Inside the Database

	Uses 'dplyr' and 'tidyeval' to fit statistical models inside
    the database. It currently supports KMeans and linear regression
    models.
	"""
	
	homepage = "https://modeldb.tidymodels.org"
	cran = "modeldb" 

	version("0.3.0", md5="c45c509581d4e891bc5f22b77e036392")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidypredict", type=("build", "run"))
