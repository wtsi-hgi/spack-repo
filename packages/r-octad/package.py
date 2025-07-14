# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROctad(RPackage):
	"""Open Cancer TherApeutic Discovery (OCTAD)

	OCTAD provides a platform for virtually screening compounds targeting precise cancer patient groups. The essential idea is to identify drugs that reverse the gene expression signature of disease by tamping down over-expressed genes and stimulating weakly expressed ones. The package offers deep-learning based reference tissue selection, disease gene expression signature creation, pathway enrichment analysis, drug reversal potency scoring, cancer cell line selection, drug enrichment analysis and in silico hit validation. It currently covers ~20,000 patient tissue samples covering 50 cancer types, and expression profiles for ~12,000 distinct compounds.
	"""
	
	bioc = "octad"

	version("1.10.0", commit="5d6122f17b00ab03f2e0258573f275f367113e81")
	version("1.4.0", commit="4fe9b7991e27617f1e62978ed53ab3762993d9aa")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-ruvseq", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-octad-db", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-edaseq", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
