# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumanomniexpress12v1bcrlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for genotyping Illumina Omni Express 12 arrays using the 'crlmm' package.
	"""
	
	bioc = "humanomniexpress12v1bCrlmm" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/humanomniexpress12v1bCrlmm_1.0.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/humanomniexpress12v1bCrlmm/humanomniexpress12v1bCrlmm_1.0.1.tar.gz"]

	version("1.0.1", md5="abdb730fc230db669e588e024ee7624b")


	# annotation