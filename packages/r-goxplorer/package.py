# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoxplorer(RPackage):
	"""Structural Exploration of the Gene Ontology (GO) Knowledge Base

	It provides an effective, efficient, and fast way to explore the Gene Ontology (GO). 
             Given a set of genes, the package contains functions to assess the GO and obtain the 
             terms associated with the genes and the levels of the GO terms. The package provides 
             functions for the three different GO ontology. We discussed the methods explicitly in 
             the following article <doi:10.1038/s41598-020-73326-3>.
	"""
	
	cran = "GOxploreR" 

	version("1.2.7", md5="bea041b29d4dc48e86a09683f526b534")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-gontr", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
