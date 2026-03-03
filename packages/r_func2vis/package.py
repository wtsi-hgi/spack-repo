# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunc2vis(RPackage):
	"""Clean and Visualize Over Expression Results from
'ConsensusPathDB'

	Provides functions to have visualization and clean-up of enriched gene ontologies (GO) terms, 
    protein complexes and pathways (obtained from multiple databases) using 'ConsensusPathDB' 
    from gene set over-expression analysis. Performs clustering of pathway based on similarity 
    of over-expressed gene sets and visualizations similar to Ingenuity Pathway Analysis (IPA) 
    when up and down regulated genes are known. The methods are described in a paper currently
    submitted by Orecchioni et al, 2020 in Nanoscale.
	"""
	
	cran = "func2vis" 

	version("1.0-3", md5="77b8efa79fa5771f79fd7ae814976367")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
