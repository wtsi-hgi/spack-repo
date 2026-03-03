# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsichomics(RPackage):
	"""Graphical Interface for Alternative Splicing Quantification, Analysis and Visualisation

	Interactive R package with an intuitive Shiny-based graphical interface for alternative splicing quantification and integrative analyses of alternative splicing and gene expression based on The Cancer Genome Atlas (TCGA), the Genotype-Tissue Expression project (GTEx), Sequence Read Archive (SRA) and user-provided data. The tool interactively performs survival, dimensionality reduction and median- and variance-based differential splicing and gene expression analyses that benefit from the incorporation of clinical and molecular sample-associated features (such as tumour stage or survival). Interactive visual access to genomic mapping and functional annotation of selected alternative splicing events is also included.
	"""
	
	homepage = "https://nuno-agostinho.github.io/psichomics/"
	bioc = "psichomics" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/psichomics_1.28.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/psichomics/psichomics_1.28.1.tar.gz"]

	version("1.28.1", md5="78be9625aca55b2c978cd56a873f7e71")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny@1.7:", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt@0.2:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-fastica", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-highcharter@0.5:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-pairsd3", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-recount", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
