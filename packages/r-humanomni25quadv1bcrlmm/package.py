# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumanomni25quadv1bcrlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for genotyping Illumina Omni2.5 Quad arrays using the 'crlmm' package.
	"""
	
	bioc = "humanomni25quadv1bCrlmm" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/humanomni25quadv1bCrlmm_1.0.2.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/humanomni25quadv1bCrlmm/humanomni25quadv1bCrlmm_1.0.2.tar.gz"]

	version("1.0.2", md5="2ee1fa7bf712d7f81a167079c975d49f")


	# annotation