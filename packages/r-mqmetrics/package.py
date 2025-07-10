# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMqmetrics(RPackage):
	"""Quality Control of Protemics Data

	The package MQmetrics (MaxQuant metrics) provides a workflow to analyze the quality and reproducibility of your proteomics mass spectrometry analysis from MaxQuant.Input data are extracted from several MaxQuant output tables and produces a pdf report. It includes several visualization tools to check numerous parameters regarding the quality of the runs. It also includes two functions to visualize the iRT peptides from Biognosys in case they were spiked in the samples.
	"""
	
	bioc = "MQmetrics" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MQmetrics_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MQmetrics/MQmetrics_1.10.0.tar.gz"]

	version("1.10.0", sha256="58c78c557937edd084a3868ea0c5036388fa3b59c78b31e2da08962964ab5396")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gghalves", type=("build", "run"))
