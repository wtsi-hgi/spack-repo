# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuman370v1ccrlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for genotyping Illumina 370k arrays using the 'crlmm' package.
	"""
	
	bioc = "human370v1cCrlmm" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/human370v1cCrlmm_1.0.2.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/human370v1cCrlmm/human370v1cCrlmm_1.0.2.tar.gz"]

	version("1.0.2", md5="9ec4192f533faee2b14484de02548075")


	# annotation