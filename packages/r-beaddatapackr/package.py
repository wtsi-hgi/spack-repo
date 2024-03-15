# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeaddatapackr(RPackage):
	"""Compression of Illumina BeadArray data

	Provides functionality for the compression and decompression of raw bead-level data from the Illumina BeadArray platform.
	"""
	
	bioc = "BeadDataPackR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BeadDataPackR_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BeadDataPackR/BeadDataPackR_1.54.0.tar.gz"]

	version("1.54.0", md5="b1e73395e4f18af4b799a1f447487a87")

