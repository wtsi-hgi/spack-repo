# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpea(RPackage):
	"""A Novel Topology-Based Pathway Enrichment Analysis Approach

	We described a novel Topology-based pathway enrichment analysis, which integrated the global position of the nodes and the topological property of the pathways in  Kyoto Encyclopedia of Genes and Genomes Database.
             We also provide some functions to obtain the latest information about pathways to finish pathway enrichment analysis using this method. 
	"""
	
	cran = "TPEA" 

	version("3.1.0", md5="21d330c31ef8384a77f40f8e349a65b4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mess", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
