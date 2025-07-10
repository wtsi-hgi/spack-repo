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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/human650v3aCrlmm_1.0.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/human650v3aCrlmm/human650v3aCrlmm_1.0.3.tar.gz"]

	version("1.0.3", sha256="8b477c64ee0f920fe0ddcd90ec783b961da268c1583a28d3be8efdb25058f717")


