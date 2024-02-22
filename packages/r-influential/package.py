# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfluential(RPackage):
	"""Identification and Classification of the Most Influential Nodes

	Contains functions for the classification and ranking of top candidate features, reconstruction of networks from
    adjacency matrices and data frames, analysis of the topology of the network 
    and calculation of centrality measures, and identification of the most
    influential nodes. Also, a function is provided for running SIRIR model, which 
    is the combination of leave-one-out cross validation technique and the conventional SIR model, on a network to unsupervisedly rank the true influence of vertices. Additionally, some functions have been provided for the assessment 
    of dependence and correlation of two network centrality measures as well as 
    the conditional probability of deviation from their corresponding means in opposite direction.
    Fred Viole and David Nawrocki (2013, ISBN:1490523995).
    Csardi G, Nepusz T (2006). "The igraph software package for complex network research." InterJournal, Complex Systems, 1695.
    Adopted algorithms and sources are referenced in function document.
	"""
	
	homepage = "https://github.com/asalavaty/influential"
	cran = "influential" 

	version("2.2.9", md5="02f6f7a56a4a0e72e19ea55beef25aee")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-coop", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
