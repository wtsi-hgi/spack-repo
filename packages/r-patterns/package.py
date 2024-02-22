# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatterns(RPackage):
	"""Deciphering Biological Networks with Patterned Heterogeneous
Measurements

	A modeling tool dedicated to biological network modeling (Bertrand and others 2020, <doi:10.1093/bioinformatics/btaa855>). It allows for single or joint modeling of, for instance, genes and proteins. It starts with the selection of the actors that will be the used in the reverse engineering upcoming step. An actor can be included in that selection based on its differential measurement (for instance gene expression or protein abundance) or on its time course profile. Wrappers for actors clustering functions and cluster analysis are provided. It also allows reverse engineering of biological networks taking into account the observed time course patterns of the actors. Many inference functions are provided and dedicated to get specific features for the inferred network such as sparsity, robust links, high confidence links or stable through resampling links. Some simulation and prediction tools are also available for cascade networks (Jung and others 2014, <doi:10.1093/bioinformatics/btt705>). Example of use with microarray or RNA-Seq data are provided.
	"""
	
	homepage = "https://fbertran.github.io/Patterns/"
	cran = "Patterns" 

	version("1.4", md5="535ceba972f917cc2840d76dd09a348e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-jetset", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mfuzz", type=("build", "run"))
	depends_on("r-movmf", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-repmis", type=("build", "run"))
	depends_on("r-selectboost", type=("build", "run"))
	depends_on("r-tnet", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
