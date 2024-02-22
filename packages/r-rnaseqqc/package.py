# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqqc(RPackage):
	"""Quality Control for RNA-Seq Data

	Functions for semi-automated quality control of bulk RNA-seq data.
	"""
	
	cran = "RNAseqQC" 

	version("0.1.4", md5="d635b54c11b875c6564c9dbf41647021")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-annotationfilter", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-vsn", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggpointdensity", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gghighlight", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
