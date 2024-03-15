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

	version("1.0.0", md5="3ac4d6867c3d5590a6308d6edff0912b")


	# annotation