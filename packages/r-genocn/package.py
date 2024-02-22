# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenocn(RPackage):
	"""genotyping and copy number study tools

	Simultaneous identification of copy number states and genotype calls for regions of either copy number variations or copy number aberrations
	"""
	
	bioc = "genoCN" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/genoCN_1.54.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/genoCN/genoCN_1.54.0.tar.gz"]

	version("1.54.0", md5="ebc7fc5cb3b5c2bcd98718a7bcd95d6a")

