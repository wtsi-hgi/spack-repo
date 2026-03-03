# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdchierarchies(RPackage):
	"""Create and (Interactively) Modify Nested Hierarchies

	Provides functionality to generate, (interactively) modify (by adding, removing and renaming nodes) and convert nested hierarchies between different formats.
  These tree like structures can be used to define for example complex hierarchical tables used for statistical disclosure control.
	"""
	
	homepage = "https://github.com/bernhard-da/sdcHierarchies"
	cran = "sdcHierarchies" 

	version("0.21.0", md5="859ca2ec7946a40ed521159cb12e65ce")

	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinytree", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
