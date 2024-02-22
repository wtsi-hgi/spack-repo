# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmdiffbamsubset(RPackage):
	"""Example ChIP-Seq data for the MMDiff package

	Subset of BAM files, including WT_2.bam, Null_2.bam, Resc_2.bam, Input.bam from the "Cfp1" experiment (see Clouaire et al., Genes Dev. 2012). Data is available under ArrayExpress accession numbers E-ERAD-79. Additionally, corresponding subset of peaks called by MACS
	"""
	
	bioc = "MMDiffBamSubset" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/MMDiffBamSubset_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/MMDiffBamSubset/MMDiffBamSubset_1.38.0.tar.gz"]

	version("1.38.0", md5="0becc66301b49b58a99efa19577ee27c")


	# experiment