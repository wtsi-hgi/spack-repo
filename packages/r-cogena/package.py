# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCogena(RPackage):
	"""co-expressed gene-set enrichment analysis

	cogena is a workflow for co-expressed gene-set enrichment analysis. It aims to discovery smaller scale, but highly correlated cellular events that may be of great biological relevance. A novel pipeline for drug discovery and drug repositioning based on the cogena workflow is proposed. Particularly, candidate drugs can be predicted based on the gene expression of disease-related data, or other similar drugs can be identified based on the gene expression of drug-related data. Moreover, the drug mode of action can be disclosed by the associated pathway analysis. In summary, cogena is a flexible workflow for various gene set enrichment analysis for co-expressed genes, with a focus on pathway/GO analysis and drug repositioning.
	"""
	
	homepage = "https://github.com/zhilongjia/cogena"
	bioc = "cogena" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cogena_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cogena/cogena_1.36.0.tar.gz"]

	version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="eec3a1b987c94647dfa5a0feac3928b302ff8ab916703f6acf37cf36307d0b44")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-kohonen", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-amap", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-biwt", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
