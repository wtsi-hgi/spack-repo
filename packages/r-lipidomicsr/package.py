# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLipidomicsr(RPackage):
	"""Elegant Tools for Processing and Visualization of Lipidomics
Data

	An elegant tool for processing and visualizing lipidomics data generated by mass spectrometry. 'LipidomicsR' simplifies channel and replicate handling while providing thorough lipid species annotation. Its visualization capabilities encompass principal components analysis plots, heatmaps, volcano plots, and radar plots, enabling concise data summarization and quality assessment. Additionally, it can generate bar plots and line plots to visualize the abundance of each lipid species.
	"""
	
	cran = "LipidomicsR" 

	version("0.1.6", md5="da0fe7b9fe2ed3527112ea5aec83d5dc")

	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ggiraph", type=("build", "run"))
	depends_on("r-rcompanion", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
