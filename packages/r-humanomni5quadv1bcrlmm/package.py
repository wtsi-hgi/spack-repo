# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumanomni5quadv1bcrlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for genotyping Illumina Omni5 Quad arrays using the 'crlmm' package.
	"""
	
	bioc = "humanomni5quadv1bCrlmm" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/humanomni5quadv1bCrlmm_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/humanomni5quadv1bCrlmm/humanomni5quadv1bCrlmm_1.0.0.tar.gz"]

	version("1.0.0", sha256="690f1454594bce8bac779ccc86bb405122cd20243ea2684a9b6d75bf1bcf8bbc")


