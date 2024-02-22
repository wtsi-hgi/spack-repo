# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApear(RPackage):
	"""Advanced Pathway Enrichment Analysis Representation

	Simplify pathway enrichment analysis results by detecting clusters
    of similar pathways and visualizing it as an enrichment network, where
    nodes and edges describe the pathways and similarity between them,
    respectively. This reduces the redundancy of the overlapping pathways and
    helps to notice the most important biological themes in the data
    (Kerseviciute and Gordevicius (2023) <doi:10.1101/2023.03.28.534514>).
	"""
	
	homepage = "https://gitlab.com/vugene/aPEAR"
	cran = "aPEAR" 

	version("1.0.0", md5="4844c2b62742b4818baa4f98e0614a5a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-bayesbio", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lsa", type=("build", "run"))
	depends_on("r-mcl", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
