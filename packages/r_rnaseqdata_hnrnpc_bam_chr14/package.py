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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RNAseqData.HNRNPC.bam.chr14_0.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RNAseqData.HNRNPC.bam.chr14/RNAseqData.HNRNPC.bam.chr14_0.40.0.tar.gz"]

	version("0.40.0", md5="9bfb7faf3c8770b15f3cf15bb670162d", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RNAseqData.HNRNPC.bam.chr14_0.40.0.tar.gz")


