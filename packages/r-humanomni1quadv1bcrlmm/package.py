# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumanomni1quadv1bcrlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for genotyping Illumina Omni1 Quad arrays using the 'crlmm' package.
	"""
	
	bioc = "humanomni1quadv1bCrlmm" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/humanomni1quadv1bCrlmm_1.0.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/humanomni1quadv1bCrlmm/humanomni1quadv1bCrlmm_1.0.3.tar.gz"]

	version("1.0.3", md5="e81b2603f37d4cda3f28cd69a7296a23")


