# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiderot(RPackage):
	"""Bibliographic Network Analysis

	Enables the user to build a citation network/graph from bibliographic data and, based on modularity and heterocitation metrics, assess the degree of awareness/cross-fertilization between two corpora/communities. This toolset is optimized for Scopus data. 
	"""
	
	cran = "Diderot" 

	version("0.13", md5="18d8763e7f4dc50e284b3309857c4286")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
