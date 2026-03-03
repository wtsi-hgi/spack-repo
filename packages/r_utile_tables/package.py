# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUtileTables(RPackage):
	"""Build Tables for Publication

	Functions for building customized ready-to-export tables for publication.
	"""
	
	homepage = "https://efinite.github.io/utile.tables/"
	cran = "utile.tables" 

	version("0.3.0", md5="c8c8494fc3b6db5277ec74db101e290c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-utile-tools@0.3:", type=("build", "run"))
