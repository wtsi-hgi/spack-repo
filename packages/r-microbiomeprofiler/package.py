# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiomeprofiler(RPackage):
	"""An R/shiny package for microbiome functional enrichment analysis

	This is an R/shiny package to perform functional enrichment analysis for microbiome data. This package was based on clusterProfiler. Moreover, MicrobiomeProfiler support KEGG enrichment analysis, COG enrichment analysis, Microbe-Disease association enrichment analysis, Metabo-Pathway analysis.
	"""
	
	homepage = "https://github.com/YuLab-SMU/MicrobiomeProfiler/"
	bioc = "MicrobiomeProfiler" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MicrobiomeProfiler_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MicrobiomeProfiler/MicrobiomeProfiler_1.8.0.tar.gz"]

	version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="4dd11f1551f9e1b5db19a28cda1e41c563efd8a34e0d81db43c63d99509f81f6")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-clusterprofiler@4.5.2:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-enrichplot", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-gson", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinycustomloader", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
