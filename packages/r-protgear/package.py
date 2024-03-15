# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProtgear(RPackage):
	"""Protein Micro Array Data Management and Interactive Visualization

	A generic three-step pre-processing package for protein microarray data. This package contains different data pre-processing procedures to allow comparison of their performance.These steps are background correction, the coefficient of variation (CV) based filtering, batch correction and normalization.
	"""
	
	homepage = "https://github.com/Keniajin/protGear"
	bioc = "protGear" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/protGear_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/protGear/protGear_1.6.0.tar.gz"]

	version("1.6.0", md5="db63dca71894a3ebbf3b8b78512bccb4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-limma@3.40.2:", type=("build", "run"))
	depends_on("r-vsn@3.54:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-ggpubr@0.4:", type=("build", "run"))
	depends_on("r-gtools@3.8.2:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-rmarkdown@2.9:", type=("build", "run"))
	depends_on("r-knitr@1.33:", type=("build", "run"))
	depends_on("r-genefilter@1.74:", type=("build", "run"))
	depends_on("r-readr@2.0.1:", type=("build", "run"))
	depends_on("r-biobase@2.52:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-kendall@2.2:", type=("build", "run"))
	depends_on("r-shiny@1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-plotly@4.9:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-htmltools@0.4:", type=("build", "run"))
	depends_on("r-flexdashboard@0.5.2:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7.1:", type=("build", "run"))
	depends_on("r-ggally@2.1.2:", type=("build", "run"))
	depends_on("r-pheatmap@1.0.12:", type=("build", "run"))
	depends_on("r-styler@1.6.1:", type=("build", "run"))
	depends_on("r-factoextra@1.0.7:", type=("build", "run"))
	depends_on("r-factominer@2.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-remotes@2.4:", type=("build", "run"))
