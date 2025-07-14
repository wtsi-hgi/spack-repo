# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuideseq(RPackage):
	"""GUIDE-seq and PEtag-seq analysis pipeline

	The package implements GUIDE-seq and PEtag-seq analysis workflow including functions for filtering UMI and reads with low coverage, obtaining unique insertion sites (proxy of cleavage sites), estimating the locations of the insertion sites, aka, peaks, merging estimated insertion sites from plus and minus strand, and performing off target search of the extended regions around insertion sites with mismatches and indels.
	"""
	
	bioc = "GUIDEseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GUIDEseq_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GUIDEseq/GUIDEseq_1.32.0.tar.gz"]

	version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="d5b01e733baf6c8a602501fb0e0e616fb041852f343a596e93bfdbc418277988")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-crisprseek", type=("build", "run"))
	depends_on("r-chippeakanno", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-iranges@2.5.5:", type=("build", "run"))
	depends_on("r-s4vectors@0.9.6:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-genomicalignments@1.7.3:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
