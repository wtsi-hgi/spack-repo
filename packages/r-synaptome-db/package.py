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

	version("0.99.16", commit="4f403fd131ce055fa87e1ba3b19aeac48a399a2a")
	version("0.99.15", commit="a78377df3d13f86dee986ef8e387d5402b2b29f2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-synaptome-data", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

