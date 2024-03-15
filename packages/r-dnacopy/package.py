# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnacopy(RPackage):
	"""DNA copy number data analysis.

	Implements the circular binary segmentation (CBS) algorithm to segment
	DNA copy number data and identify genomic regions with abnormal copy
	number."""

	bioc = "DNAcopy"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DNAcopy_1.76.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DNAcopy/DNAcopy_1.76.0.tar.gz"]

	version("1.76.0", md5="1b80859f79a39def302664f11b91a98f")

