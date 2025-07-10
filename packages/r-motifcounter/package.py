# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotifcounter(RPackage):
	"""R package for analysing TFBSs in DNA sequences

	'motifcounter' provides motif matching, motif counting and motif enrichment functionality based on position frequency matrices. The main features of the packages include the utilization of higher-order background models and accounting for self-overlapping motif matches when determining motif enrichment. The background model allows to capture dinucleotide (or higher-order nucleotide) composition adequately which may reduced model biases and misleading results compared to using simple GC background models. When conducting a motif enrichment analysis based on the motif match count, the package relies on a compound Poisson distribution or alternatively a combinatorial model. These distribution account for self-overlapping motif structures as exemplified by repeat-like or palindromic motifs, and allow to determine the p-value and fold-enrichment for a set of observed motif matches.
	"""
	
	bioc = "motifcounter" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/motifcounter_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/motifcounter/motifcounter_1.26.0.tar.gz"]

	version("1.26.0", sha256="c75ffe58a934b30f194fe93dc498751d0c3776af4958e9a152a2423dde40e259")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
