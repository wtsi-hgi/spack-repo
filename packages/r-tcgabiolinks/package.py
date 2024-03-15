# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgabiolinks(RPackage):
	"""TCGAbiolinks: An R/Bioconductor package for integrative analysis with GDC data

	The aim of TCGAbiolinks is : i) facilitate the GDC open-access data retrieval, ii) prepare the data using the appropriate pre-processing strategies, iii) provide the means to carry out different standard analyses and iv) to easily reproduce earlier research results. In more detail, the package provides multiple methods for analysis (e.g., differential expression analysis, identifying differentially methylated regions) and methods for visualization (e.g., survival plots, volcano plots, starburst plots) in order to easily develop complete analysis pipelines.
	"""
	
	homepage = "https://github.com/BioinformaticsFMRP/TCGAbiolinks"
	bioc = "TCGAbiolinks" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TCGAbiolinks_2.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TCGAbiolinks/TCGAbiolinks_2.30.0.tar.gz"]

	version("2.30.0", md5="91536d6234ebd992dac8102393c363d0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-downloader@0.4:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-xml@3.98:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite@1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rvest@0.3:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.4:", type=("build", "run"))
	depends_on("r-tcgabiolinksgui-data@1.15.1:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
