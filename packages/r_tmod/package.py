# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmod(RPackage):
	"""Feature Set Enrichment Analysis for Metabolomics and
Transcriptomics

	Methods and feature set definitions for feature or gene set
  enrichment analysis in transcriptional and metabolic profiling data.
  Package includes tests for enrichment based on ranked lists of features,
  functions for visualisation and multivariate functional analysis. See Zyla et al (2019)
  <doi:10.1093/bioinformatics/btz447>.
	"""
	
	homepage = "https://tmod.online"
	cran = "tmod" 

	version("0.50.13", md5="ed0010f289814b38457c9b19d01c697b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-beeswarm", type=("build", "run"))
	depends_on("r-tagcloud", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-plotwidgets", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
