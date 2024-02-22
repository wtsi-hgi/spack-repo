# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuman650v3acrlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for genotyping Illumina 650k arrays using the 'crlmm' package.
	"""
	
	bioc = "human650v3aCrlmm" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/human650v3aCrlmm_1.0.3.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/human650v3aCrlmm/human650v3aCrlmm_1.0.3.tar.gz"]

	version("1.0.3", md5="4b0de367ccc0f7499dcffe21ef1893c2")


	# annotation