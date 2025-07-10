# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTissueenrich(RPackage):
	"""Tissue-specific gene enrichment analysis

	The TissueEnrich package is used to calculate enrichment of tissue-specific genes in a set of input genes. For example, the user can input the most highly expressed genes from RNA-Seq data, or gene co-expression modules to determine which tissue-specific genes are enriched in those datasets. Tissue-specific genes were defined by processing RNA-Seq data from the Human Protein Atlas (HPA) (Uhlén et al. 2015), GTEx (Ardlie et al. 2015), and mouse ENCODE (Shen et al. 2012) using the algorithm from the HPA (Uhlén et al. 2015).The hypergeometric test is being used to determine if the tissue-specific genes are enriched among the input genes. Along with tissue-specific gene enrichment, the TissueEnrich package can also be used to define tissue-specific genes from expression datasets provided by the user, which can then be used to calculate tissue-specific gene enrichments.
	"""
	
	bioc = "TissueEnrich" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TissueEnrich_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TissueEnrich/TissueEnrich_1.22.0.tar.gz"]

	version("1.22.0", sha256="d258d871cd7463b80af875d214dfa7a76abc9bb13c7f13604ffe04bf0dbc8c8f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ensurer@1.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.6.5:", type=("build", "run"))
	depends_on("r-gseabase@1.38.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.3:", type=("build", "run"))
	depends_on("r-tidyr@0.8:", type=("build", "run"))
