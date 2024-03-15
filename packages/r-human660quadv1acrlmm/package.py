# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuman660quadv1acrlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for genotyping Illumina 660kQuad arrays using the 'crlmm' package.
	"""
	
	bioc = "human660quadv1aCrlmm" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/human660quadv1aCrlmm_1.0.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/human660quadv1aCrlmm/human660quadv1aCrlmm_1.0.3.tar.gz"]

	version("1.0.3", md5="5fd2d94a462e150c888f13c5c0975c36")


	# annotation