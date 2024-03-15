# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuman1mv1ccrlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata fast genotyping Illumina 1M arrays using the 'crlmm' package.
	"""
	
	bioc = "human1mv1cCrlmm" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/human1mv1cCrlmm_1.0.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/human1mv1cCrlmm/human1mv1cCrlmm_1.0.3.tar.gz"]

	version("1.0.3", md5="b9f638c7b0ede50cb070f1bae85eb4dc")


	# annotation