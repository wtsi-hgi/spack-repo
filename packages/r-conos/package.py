# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConos(RPackage):
	"""Clustering on Network of Samples

	Wires together large collections of single-cell RNA-seq datasets, which allows for both the identification of recurrent cell clusters and the propagation of information between datasets in multi-sample or atlas-scale collections. 'Conos' focuses on the uniform mapping of homologous cell types across heterogeneous sample collections. For instance, users could investigate a collection of dozens of peripheral blood samples from cancer patients combined with dozens of controls, which perhaps includes samples of a related tissue such as lymph nodes. This package interacts with data available through the 'conosPanel' package, which is available in a 'drat' repository. To access this data package, see the instructions at <https://github.com/kharchenkolab/conos>. The size of the 'conosPanel' package is approximately 12 MB.
	"""
	
	homepage = "https://github.com/kharchenkolab/conos"
	cran = "conos" 

	version("1.5.2", md5="ebbd6a030dabdbcff607dee0bd937081")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-leidenalg", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-n2r", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-sccore@1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
