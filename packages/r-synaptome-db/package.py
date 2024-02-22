# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynaptomeDb(RPackage):
	"""Synamptosome Proteome Database

	The package contains local copy of the Synaptic proteome database. On top of this it provide a set of utility R functions to query and analyse its content. It allows extraction of information for specific genes and building the protein-protein interaction graph for gene sets, synaptic compartments, and brain regions.
	"""
	
	bioc = "synaptome.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/synaptome.db_0.99.15.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/synaptome.db/synaptome.db_0.99.15.tar.gz"]

	version("0.99.15", md5="7ed11d61ac8dca86372eeec59b5ab03b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-synaptome-data", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

	# annotation