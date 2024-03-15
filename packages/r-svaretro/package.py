# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvaretro(RPackage):
	"""Retrotransposed transcript detection from structural variants

	svaRetro contains functions for detecting retrotransposed transcripts (RTs) from structural variant calls. It takes structural variant calls in GRanges of breakend notation and identifies RTs by exon-exon junctions and insertion sites. The candidate RTs are reported by events and annotated with information of the inserted transcripts.
	"""
	
	bioc = "svaRetro" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/svaRetro_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/svaRetro/svaRetro_1.8.0.tar.gz"]

	version("1.8.0", md5="56da2ed056a7078a5d9f2883885d5be5")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-structuralvariantannotation", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
