# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGseavis(RPackage):
	"""Implement for 'GSEA' Enrichment Visualization

	Mark your interesting genes on plot and support more parameters to handle your own gene set enrichment analysis plot.
	"""
	
	homepage = "https://github.com/junjunlab/GseaVis"
	cran = "GseaVis" 

	version("0.0.5", md5="bbee0d64a60043b4a251a5ba15505d70")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-aplot", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpp", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
