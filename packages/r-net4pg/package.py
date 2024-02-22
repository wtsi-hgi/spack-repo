# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNet4pg(RPackage):
	"""Handle Ambiguity of Protein Identifications from Shotgun
Proteomics

	In shotgun proteomics, shared peptides (i.e., peptides that might 
    originate from different proteins sharing homology, from different 
    proteoforms due to alternative mRNA splicing, post-translational 
    modifications, proteolytic cleavages, and/or allelic variants) represent a
    major source of ambiguity in protein identifications. The 'net4pg' package 
    allows to assess and handle ambiguity of protein identifications. It 
    implements methods for two main applications. First, it allows to represent
    and quantify ambiguity of protein identifications by means of graph 
    connected components (CCs). In graph theory, CCs are defined as the largest
    subgraphs in which any two vertices are connected to each other by a path 
    and not connected to any other of the vertices in the supergraph. Here, 
    proteins sharing one or more peptides are thus gathered in the same CC 
    (multi-protein CC), while unambiguous protein identifications constitute CCs 
    with a single protein vertex (single-protein CCs). Therefore, the proportion
    of single-protein CCs and the size of multi-protein CCs can be used to
    measure the level of ambiguity of protein identifications. The package
    implements a strategy to efficiently calculate graph connected
    components on large datasets and allows to visually inspect them.
    Secondly, the 'net4pg' package allows to exploit the increasing
    availability of matched transcriptomic and proteomic datasets to
    reduce ambiguity of protein identifications. More precisely, it
    implement a transcriptome-based filtering strategy fundamentally
    consisting in the removal of those proteins whose corresponding
    transcript is not expressed in the sample-matched transcriptome. The
    underlying assumption is that, according to the central dogma of
    biology, there can be no proteins without the corresponding
    transcript. Most importantly, the package allows to visually inspect
    the effect of the filtering on protein identifications and quantify
    ambiguity before and after filtering by means of graph connected
    components. As such, it constitutes a reproducible and transparent
    method to exploit transcriptome information to enhance protein
    identifications. All methods implemented in the 'net4pg' package are fully 
    described in Fancello and Burger (2022) <doi:10.1186/s13059-022-02701-2>.
	"""
	
	homepage = "https://github.com/laurafancello/net4pg"
	cran = "net4pg" 

	version("0.1.1", md5="1eb5dc8b6c1acf683dde042fd3cd0992")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
