# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDamefinder(RPackage):
	"""Finds DAMEs - Differential Allelicly MEthylated regions

	'DAMEfinder' offers functionality for taking methtuple or bismark outputs to calculate ASM scores and compute DAMEs. It also offers nice visualization of methyl-circle plots.
	"""
	
	bioc = "DAMEfinder" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DAMEfinder_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DAMEfinder/DAMEfinder_1.14.0.tar.gz"]

	version("1.14.0", md5="0f99003a20995ebd0c15fce1a407765f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-bumphunter", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
