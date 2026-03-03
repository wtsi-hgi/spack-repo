# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDespace(RPackage):
	"""DESpace: a framework to discover spatially variable genes

	Intuitive framework for identifying spatially variable genes (SVGs) via edgeR, a popular method for performing differential expression analyses. Based on pre-annotated spatial clusters as summarized spatial information, DESpace models gene expression using a negative binomial (NB), via edgeR, with spatial clusters as covariates. SVGs are then identified by testing the significance of spatial clusters. The method is flexible and robust, and is faster than the most SV methods. Furthermore, to the best of our knowledge, it is the only SV approach that allows: - performing a SV test on each individual spatial cluster, hence identifying the key regions of the tissue affected by spatial variability; - jointly fitting multiple samples, targeting genes with consistent spatial patterns across replicates.
	"""
	
	homepage = "https://github.com/peicai/DESpace"
	bioc = "DESpace" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DESpace_1.2.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DESpace/DESpace_1.2.1.tar.gz"]

	version("1.2.1", md5="98a7395caa0d843520f62f06386483b9")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
