# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnapath(RPackage):
	"""Differential Network Analysis using Gene Pathways

	Integrates pathway information into the differential network analysis of two gene expression datasets as described in Grimes, Potter, and Datta (2019) <doi:10.1038/s41598-019-41918-3>. Provides summary functions to break down the results at the pathway, gene, or individual connection level. The differential networks for each pathway of interest can be plotted, and the visualization will highlight any differentially expressed genes and all of the gene-gene associations that are significantly differentially connected.
	"""
	
	cran = "dnapath" 

	version("0.7.4", md5="f686a6ce858fa18c51509f903c010090")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-seqnet", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-wcorr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
