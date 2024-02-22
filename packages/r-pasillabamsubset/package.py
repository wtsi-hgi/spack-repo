# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPasillabamsubset(RPackage):
	"""Subset of BAM files from "Pasilla" experiment

	Subset of BAM files untreated1.bam (single-end reads) and untreated3.bam (paired-end reads) from "Pasilla" experiment (Pasilla knock-down by Brooks et al., Genome Research 2011). See the vignette in the pasilla data package for how BAM files untreated1.bam and untreated3.bam were obtained from the RNA-Seq read sequence data that is provided by NCBI Gene Expression Omnibus under accession numbers GSM461176 to GSM461181.  Also contains the DNA sequence for fly chromosome 4 to which the reads can be mapped.
	"""
	
	bioc = "pasillaBamSubset" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/pasillaBamSubset_0.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/pasillaBamSubset/pasillaBamSubset_0.40.0.tar.gz"]

	version("0.40.0", md5="8fd05eac2d37650e157871908cbaf306")


	# experiment