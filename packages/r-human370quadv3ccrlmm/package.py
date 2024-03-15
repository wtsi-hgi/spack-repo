# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuman370quadv3ccrlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for genotyping Illumina 370kQuad arrays using the 'crlmm' package.
	"""
	
	bioc = "human370quadv3cCrlmm" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/human370quadv3cCrlmm_1.0.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/human370quadv3cCrlmm/human370quadv3cCrlmm_1.0.3.tar.gz"]

	version("1.0.3", md5="33c3ccc3793ed95647418b746a5177f9")


	# annotation