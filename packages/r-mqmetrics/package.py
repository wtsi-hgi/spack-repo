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

	version("1.10.0", commit="86b96435866214f4b9d91790fac56cf402b31ffe")

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
