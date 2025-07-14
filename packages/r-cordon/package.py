# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCordon(RPackage):
	"""Codon Usage Analysis and Prediction of Gene Expressivity

	Tool for analysis of codon usage in various unannotated or KEGG/COG annotated DNA sequences. Calculates different measures of CU bias and CU-based predictors of gene expressivity, and performs gene set enrichment analysis for annotated sequences. Implements several methods for visualization of CU and enrichment analysis results.
	"""
	
	homepage = "https://github.com/BioinfoHR/coRdon"
	bioc = "coRdon" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/coRdon_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/coRdon/coRdon_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="0b3ccdf6e515ec452ef4284d96d5beb7c6f96cd6f3f23d3a3653b9e57a4f03a3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
