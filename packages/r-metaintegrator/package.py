# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaintegrator(RPackage):
	"""Meta-Analysis of Gene Expression Data

	A pipeline for the meta-analysis  of gene expression data. We have
	assembled several analysis and plot functions to
    perform integrated multi-cohort analysis of gene expression data (meta-
    analysis). Methodology described in:
	<http://biorxiv.org/content/early/2016/08/25/071514>.
	"""
	
	homepage = "http://biorxiv.org/content/early/2016/08/25/071514"
	cran = "MetaIntegrator" 

	version("2.1.3", md5="38c11bd9a64f07e316acf8ebb3e4d895")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-rmeta", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rmisc", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rmysql", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-geometadb", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-coconut", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-manhattanly", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-hgnchelper", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
