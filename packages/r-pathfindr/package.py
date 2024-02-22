# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathfindr(RPackage):
	"""Enrichment Analysis Utilizing Active Subnetworks

	Enrichment analysis enables researchers to uncover mechanisms 
    underlying a phenotype. However, conventional methods for enrichment 
    analysis do not take into account protein-protein interaction information, 
    resulting in incomplete conclusions. pathfindR is a tool for enrichment 
    analysis utilizing active subnetworks. The main function identifies active 
    subnetworks in a protein-protein interaction network using a user-provided 
    list of genes and associated p values. It then performs enrichment analyses 
    on the identified subnetworks, identifying enriched terms (i.e. pathways or, 
    more broadly, gene sets) that possibly underlie the phenotype of interest.
    pathfindR also offers functionalities to cluster the enriched terms and 
    identify representative terms in each cluster, to score the enriched terms 
    per sample and to visualize analysis results. The enrichment, clustering and 
    other methods implemented in pathfindR are described in detail in 
    Ulgen E, Ozisik O, Sezerman OU. 2019. pathfindR: An R Package for 
    Comprehensive Identification of Enriched Pathways in Omics Data Through 
    Active Subnetworks. Front. Genet. <doi:10.3389/fgene.2019.00858>.
	"""
	
	homepage = "https://egeulgen.github.io/pathfindR/"
	cran = "pathfindR" 

	version("2.3.1", md5="3a4998890d0b3ce241a6075c9c3de2f8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-pathfindr-data@2:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggupset", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-msigdbr", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
