# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPasilla(RPackage):
	"""Data package with per-exon and per-gene read counts of RNA-seq samples of Pasilla knock-down by Brooks et al., Genome Research 2011.

	This package provides per-exon and per-gene read counts computed for selected genes from RNA-seq data that were presented in the article "Conservation of an RNA regulatory map between Drosophila and mammals" by Brooks AN, Yang L, Duff MO, Hansen KD, Park JW, Dudoit S, Brenner SE, Graveley BR, Genome Res. 2011 Feb;21(2):193-202, Epub 2010 Oct 4, PMID: 20921232. The experiment studied the effect of RNAi knockdown of Pasilla, the Drosophila melanogaster ortholog of mammalian NOVA1 and NOVA2, on the transcriptome.  The package vignette describes how the data provided here were derived from the RNA-Seq read sequence data that are provided by NCBI Gene Expression Omnibus under accession numbers GSM461176 to GSM461181.
	"""
	
	bioc = "pasilla" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/pasilla_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/pasilla/pasilla_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="a0594fbfe8292a5549a7deda36bcc3d27a9e1dd18b5c1f6af02f4a7cd622ea35")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dexseq", type=("build", "run"))

