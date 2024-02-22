# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneselectr(RPackage):
	"""'GeneSelectR' - Comprehensive Feature Selection Workflow for
Bulk RNAseq Datasets

	The workflow is a versatile R package designed for comprehensive feature selection in bulk RNAseq datasets. Its key innovation lies in the seamless integration of the 'Python' 'scikit-learn' (<https://scikit-learn.org/stable/index.html>) machine learning framework with R-based bioinformatics tools. 'GeneSelectR' performs robust Machine Learning-driven (ML) feature selection while leveraging 'Gene Ontology' (GO) enrichment analysis as described by Thomas PD et al. (2022) <doi:10.1002/pro.4218>, using 'clusterProfiler' (Wu et al., 2021) <doi:10.1016/j.xinn.2021.100141> and semantic similarity analysis powered by 'simplifyEnrichment' (Gu, Huebschmann, 2021) <doi:10.1016/j.gpb.2022.04.008>. This combination of methodologies optimizes computational and biological insights for analyzing complex RNAseq datasets.
	"""
	
	homepage = "https://github.com/dzhakparov/GeneSelectR"
	cran = "GeneSelectR" 

	version("1.0.1", md5="594225773dfd4487c201adab9fc394f9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cowplot@1.1.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.3:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-reticulate@1.28:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-testthat@3:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-tmod@0.50.13:", type=("build", "run"))
