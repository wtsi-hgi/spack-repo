# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoonlight2r(RPackage):
	"""Identify oncogenes and tumor suppressor genes from omics data

	The understanding of cancer mechanism requires the identification of genes playing a role in the development of the pathology and the characterization of their role (notably oncogenes and tumor suppressors). We present an updated version of the R/bioconductor package called MoonlightR, namely Moonlight2R, which returns a list of candidate driver genes for specific cancer types on the basis of omics data integration. The Moonlight framework contains a primary layer where gene expression data and information about biological processes are integrated to predict genes called oncogenic mediators, divided into putative tumor suppressors and putative oncogenes. This is done through functional enrichment analyses, gene regulatory networks and upstream regulator analyses to score the importance of well-known biological processes with respect to the studied cancer type. By evaluating the effect of the oncogenic mediators on biological processes or through random forests, the primary layer predicts two putative roles for the oncogenic mediators: i) tumor suppressor genes (TSGs) and ii) oncogenes (OCGs). As gene expression data alone is not enough to explain the deregulation of the genes, a second layer of evidence is needed. We have automated the integration of a secondary mutational layer through new functionalities in Moonlight2R. These functionalities analyze mutations in the cancer cohort and classifies these into driver and passenger mutations using the driver mutation prediction tool, CScape-somatic. Those oncogenic mediators with at least one driver mutation are retained as the driver genes. As a consequence, this methodology does not only identify genes playing a dual role (e.g. TSG in one cancer type and OCG in another) but also helps in elucidating the biological processes underlying their specific roles. In particular, Moonlight2R can be used to discover OCGs and TSGs in the same cancer type. This may for instance help in answering the question whether some genes change role between early stages (I, II) and late stages (III, IV). In the future, this analysis could be useful to determine the causes of different resistances to chemotherapeutic treatments.
	"""
	
	homepage = "https://github.com/ELELAB/Moonlight2R"
	bioc = "Moonlight2R"

	version("1.6.0", commit="8faf1a1ae5a2ec0f2ecce79d836b697aace6cd84")
	version("1.0.0", commit="f5bfcb9a3c80ab405755a00b9e7ef06fc9989fd9")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-parmigene", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-hiver", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rismed", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fuzzyjoin", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-seqminer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyheatmap", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-easypubmed", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
