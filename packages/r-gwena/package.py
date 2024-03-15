# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwena(RPackage):
	"""Pipeline for augmented co-expression analysis

	The development of high-throughput sequencing led to increased use of co-expression analysis to go beyong single feature (i.e. gene) focus. We propose GWENA (Gene Whole co-Expression Network Analysis) , a tool designed to perform gene co-expression network analysis and explore the results in a single pipeline. It includes functional enrichment of modules of co-expressed genes, phenotypcal association, topological analysis and comparison of networks configuration between conditions.
	"""
	
	bioc = "GWENA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GWENA_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GWENA/GWENA_1.12.0.tar.gz"]

	version("1.12.0", md5="8f1bd435deae9546d0ec3f8605a0b682")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-wgcna@1.67:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-dynamictreecut@1.63.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-gprofiler2@0.1.6:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-netrep@1.2.1:", type=("build", "run"))
	depends_on("r-igraph@1.2.4.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rlist@0.4.6.1:", type=("build", "run"))
	depends_on("r-matrixstats@0.55:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.14.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-cluster@2.1:", type=("build", "run"))
