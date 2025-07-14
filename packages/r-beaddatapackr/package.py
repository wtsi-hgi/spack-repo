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

    version("1.60.0", tag="RELEASE_3_21")
	version("1.54.0", sha256="bf8334ad6e6b7a7df914ceb0e4331fac47f65ee0a9ffa9d3face616cf86dd769")

