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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MMDiffBamSubset_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MMDiffBamSubset/MMDiffBamSubset_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="b7bf8fa4c70037ee7b41b6af65c20adbaee5a91234ec5e06c3fc57f9096390ab")


