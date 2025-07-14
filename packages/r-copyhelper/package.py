# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopyhelper(RPackage):
	"""Helper files for CopywriteR

	This package contains the helper files that are required to run the Bioconductor package CopywriteR. It contains pre-assembled 1kb bin GC-content and mappability files for the reference genomes hg18, hg19, hg38, mm9 and mm10. In addition, it contains a blacklist filter to remove regions that display CNV. Files are stored as GRanges objects from the GenomicRanges Bioconductor package.
	"""
	
	bioc = "CopyhelpeR"

	version("1.40.0", commit="881df9035b3b6527fe02387c5ea635eb330751c4")
	version("1.34.0", commit="9857e4b53b40f228d61c0d2f349dd2d8aa1190c0")

	depends_on("r@3.5:", type=("build", "run"))

