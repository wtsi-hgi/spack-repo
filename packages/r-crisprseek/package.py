# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprseek(RPackage):
	"""Design of target-specific guide RNAs in CRISPR-Cas9, genome-editing systems

	The package includes functions to find potential guide RNAs for the CRISPR editing system including Base Editors and the Prime Editor for input target sequences, optionally filter guide RNAs without restriction enzyme cut site, or without paired guide RNAs, genome-wide search for off-targets, score, rank, fetch flank sequence and indicate whether the target and off-targets are located in exon region or not. Potential guide RNAs are annotated with total score of the top5 and topN off-targets, detailed topN mismatch sites, restriction enzyme cut sites, and paired guide RNAs. The package also output indels and their frequencies for Cas9 targeted sites.
	"""
	
	bioc = "CRISPRseek"

	version("1.48.0", commit="d7b7729951d334f0078429b299d43a6dbbafedac")
	version("1.42.0", commit="bd578a555ca828b380718e15ec7c7b0866cf1022")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-mltools", type=("build", "run"))
