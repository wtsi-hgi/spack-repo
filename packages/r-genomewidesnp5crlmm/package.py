# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomewidesnp5crlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for fast genotyping Affymetrix GenomeWideSnp_5 arrays using the 'crlmm' package. Annotation build is hg19.
	"""
	
	bioc = "genomewidesnp5Crlmm" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/genomewidesnp5Crlmm_1.0.6.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/genomewidesnp5Crlmm/genomewidesnp5Crlmm_1.0.6.tar.gz"]

	version("1.0.6", md5="cc24140cd17758b8e09f4fe6c931526a")


