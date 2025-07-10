# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprbowtie(RPackage):
	"""Bowtie-based alignment of CRISPR gRNA spacer sequences

	Provides a user-friendly interface to map on-targets and off-targets of CRISPR gRNA spacer sequences using bowtie. The alignment is fast, and can be performed using either commonly-used or custom CRISPR nucleases. The alignment can work with any reference or custom genomes. Both DNA- and RNA-targeting nucleases are supported.
	"""
	
	homepage = "https://github.com/crisprVerse/crisprBowtie"
	bioc = "crisprBowtie" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/crisprBowtie_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/crisprBowtie/crisprBowtie_1.6.0.tar.gz"]

	version("1.6.0", sha256="cad58133c53a6120272387a1edde6c70360ab182f596d59d4435fbc9122c02e6")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-crisprbase@0.99.15:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rbowtie", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
