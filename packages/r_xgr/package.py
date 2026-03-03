# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXgr(RPackage):
	"""XGR: eXploring Genomic Relations at the gene, SNP and genomic region level through enrichment analysis, similarity analysis and network analysis"""
	
	git = "https://github.com/hfang-bristol/XGR.git" 

	version("1.1.9", commit="7b947080b310363e2b82c24c82d3394335906f54")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-suprahex", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggnetwork", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-osfr", type=("build", "run"))
	depends_on("r-rcircos", type=("build", "run"))
