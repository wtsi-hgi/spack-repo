# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworktoolbox(RPackage):
	"""Methods and Measures for Brain, Cognitive, and Psychometric
Network Analysis

	Implements network analysis and graph theory measures used in neuroscience, cognitive science, and psychology. Methods include various filtering methods and approaches such as threshold, dependency (Kenett, Tumminello, Madi, Gur-Gershgoren, Mantegna, & Ben-Jacob, 2010 <doi:10.1371/journal.pone.0015032>), Information Filtering Networks (Barfuss, Massara, Di Matteo, & Aste, 2016 <doi:10.1103/PhysRevE.94.062306>), and Efficiency-Cost Optimization (Fallani, Latora, & Chavez, 2017 <doi:10.1371/journal.pcbi.1005305>). Brain methods include the recently developed Connectome Predictive Modeling (see references in package). Also implements several network measures including local network characteristics (e.g., centrality), community-level network characteristics (e.g., community centrality), global network characteristics (e.g., clustering coefficient), and various other measures associated with the reliability and reproducibility of network analysis. 
	"""
	
	cran = "NetworkToolbox" 

	version("1.4.2", md5="3a73b0027a9e41354b21e07f5ba23b08")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-r-matlab", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pwr", type=("build", "run"))
	depends_on("r-isingfit", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
