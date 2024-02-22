# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqsetvis(RPackage):
	"""Set Based Visualizations for Next-Gen Sequencing Data

	seqsetvis enables the visualization and analysis of sets of genomic sites in next gen sequencing data. Although seqsetvis was designed for the comparison of mulitple ChIP-seq samples, this package is domain-agnostic and allows the processing of multiple genomic coordinate files (bed-like files) and signal files (bigwig files pileups from bam file).
	"""
	
	bioc = "seqsetvis" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/seqsetvis_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/seqsetvis/seqsetvis_1.22.0.tar.gz"]

	version("1.22.0", md5="0119c8a5e2475e3a0d35059b3c35dfd6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-eulerr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
