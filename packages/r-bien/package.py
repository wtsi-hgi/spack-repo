# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBien(RPackage):
	"""Tools for Accessing the Botanical Information and Ecology
Network Database

	Provides Tools for Accessing the Botanical Information and Ecology Network Database.  The BIEN database contains cleaned and standardized botanical data including occurrence, trait, plot and taxonomic data (See <https://bien.nceas.ucsb.edu/bien/> for more Information).  This package provides functions that query the BIEN database by constructing and executing optimized SQL queries.
	"""
	
	cran = "BIEN" 

	version("1.2.6", md5="2d7089c79588c49c36ba166acb8f50fc")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-rpostgresql", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-fasterize", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
