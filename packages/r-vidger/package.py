# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVidger(RPackage):
	"""Create rapid visualizations of RNAseq data in R

	The aim of vidger is to rapidly generate information-rich visualizations for the interpretation of differential gene expression results from three widely-used tools: Cuffdiff, DESeq2, and edgeR.
	"""
	
	homepage = "https://github.com/btmonier/vidger"
	bioc = "vidger"

	version("1.28.0", commit="41a3c148a43f8722cf0e8616fdd6fcac805afebe")
	version("1.22.0", commit="c0d4628049dea1e1cbc567c5c5a916b093939570")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
