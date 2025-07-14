# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasycelltype(RPackage):
	"""Annotate cell types for scRNA-seq data

	We developed EasyCellType which can automatically examine the input marker lists obtained from existing software such as Seurat over the cell markerdatabases. Two quantification approaches to annotate cell types are provided: Gene set enrichment analysis (GSEA) and a modified versio of Fisher's exact test. The function presents annotation recommendations in graphical outcomes: bar plots for each cluster showing candidate cell types, as well as a dot plot summarizing the top 5 significant annotations for each cluster.
	"""
	
	bioc = "EasyCellType" 

	version("1.10.0", tag="RELEASE_3_21")
	version("1.4.0", commit="a2e92b6cd217fb92d6970996932847af7b9eb4fb")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
