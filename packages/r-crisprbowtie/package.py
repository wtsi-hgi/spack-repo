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

	version("1.12.0", commit="0ce73a4282909463d937a16c76372dd365738c70")
	version("1.6.0", commit="8e28fd8b1286d6257315538ee7144319c068551a")

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
