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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/humanomni25quadv1bCrlmm_1.0.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/humanomni25quadv1bCrlmm/humanomni25quadv1bCrlmm_1.0.2.tar.gz"]

	version("1.0.2", sha256="d0c184e9e4d855e22ca322eadfacce193b0636bf1a45cffcfadd9de293c417e6")


