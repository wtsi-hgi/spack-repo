# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmsa(RPackage):
	"""Plot Multiple Sequence Alignment using 'ggplot2'

	A visual exploration tool for multiple sequence alignment and associated data. Supports MSA of DNA, RNA, and protein sequences using 'ggplot2'. Multiple sequence alignment can easily be combined with other 'ggplot2' plots, such as phylogenetic tree Visualized by 'ggtree', boxplot, genome map and so on. More features: visualization of sequence logos, sequence bundles, RNA secondary structures and detection of sequence recombinations.
	"""
	
	homepage = "https://doi.org/10.1093/bib/bbac222(paper)"
	bioc = "ggmsa" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ggmsa_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ggmsa/ggmsa_1.8.0.tar.gz"]

	version("1.8.0", md5="1faea3aedc093bb7e151208c9a11b60c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-aplot", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggalt", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r4rna", type=("build", "run"))
	depends_on("r-seqmagick", type=("build", "run"))
	depends_on("r-statebins", type=("build", "run"))
	depends_on("r-ggtree@1.17.1:", type=("build", "run"))
