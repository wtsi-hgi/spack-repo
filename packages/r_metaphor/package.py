# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaphor(RPackage):
	"""Metabolic Pathway Analysis of RNA

	MetaPhOR was developed to enable users to assess metabolic dysregulation using transcriptomic-level data (RNA-sequencing and Microarray data) and produce publication-quality figures. A list of differentially expressed genes (DEGs), which includes fold change and p value, from DESeq2 or limma, can be used as input, with sample size for MetaPhOR, and will produce a data frame of scores for each KEGG pathway. These scores represent the magnitude and direction of transcriptional change within the pathway, along with estimated p-values.MetaPhOR then uses these scores to visualize metabolic profiles within and between samples through a variety of mechanisms, including: bubble plots, heatmaps, and pathway models.
	"""
	
	bioc = "MetaPhOR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MetaPhOR_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MetaPhOR/MetaPhOR_1.4.0.tar.gz"]

	version("1.4.0", md5="311e286126427130d127b23a77b3b6f4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-recordlinkage", type=("build", "run"))
	depends_on("r-rcy3", type=("build", "run"))
