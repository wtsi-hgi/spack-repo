# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgad(RPackage):
	"""Extending guilt by association by degree

	The package implements a series of highly efficient tools to calculate functional properties of networks based on guilt by association methods.
	"""
	
	bioc = "EGAD"

	version("1.36.0", commit="8b636bb83b80b18b14e19f691b68fe0482bc4758")
	version("1.30.0", commit="d5292778e97fefc422c58c5d9c05b653b4a9897c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
