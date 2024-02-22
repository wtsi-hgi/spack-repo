# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDm(RPackage):
	"""Relational Data Models

	Provides tools for working with multiple related
    tables, stored as data frames or in a relational database.  Multiple
    tables (data and metadata) are stored in a compound object, which can
    then be manipulated with a pipe-friendly syntax.
	"""
	
	homepage = "https://dm.cynkra.com/"
	cran = "dm" 

	version("1.0.10", md5="4d3a140e9741e483e9834c18e72e60d5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-cli@2.2:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-vctrs@0.3.2:", type=("build", "run"))
