# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCepa(RPackage):
	"""Centrality-Based Pathway Enrichment

	It aims to find significant pathways through 
    network topology information. It has several advantages compared 
    with current pathway enrichment tools. First, pathway node instead 
    of single gene is taken as the basic unit when analysing networks 
    to meet the fact that genes must be constructed into complexes to 
    hold normal functions. Second, multiple network centrality measures are 
    applied simultaneously to measure importance of nodes from different 
    aspects to make a full view on the biological system. CePa extends 
    standard pathway enrichment methods, which include both over-representation 
    analysis procedure and gene-set analysis procedure. 
    <doi:10.1093/bioinformatics/btt008>.
	"""
	
	homepage = "https://github.com/jokergoo/CePa"
	cran = "CePa" 

	version("0.8.0", md5="5e0b7a832876302ddae3432f8bf89535")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph@0.6:", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
