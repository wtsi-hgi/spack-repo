# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqdataHnrnpcBamChr14(RPackage):
	"""Aligned reads from RNAseq experiment: Transcription profiling by high throughput sequencing of HNRNPC knockdown and control HeLa cells

	The package contains 8 BAM files, 1 per sequencing run. Each BAM file was obtained by (1) aligning the reads (paired-end) to the full hg19 genome with TopHat2, and then (2) subsetting to keep only alignments on chr14. See accession number E-MTAB-1147 in the ArrayExpress database for details about the experiment, including links to the published study (by Zarnack et al., 2012) and to the FASTQ files.
	"""
	
	homepage = "http://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-1147/"
	bioc = "RNAseqData.HNRNPC.bam.chr14"

	version("0.46.0", commit="0282a216072ee0e8f0f7fe627f01ca4d1ec53d50")
	version("0.40.0", commit="5e39e1e7b19d3f4b1beeaf44a9fa9af832ed85b6")


