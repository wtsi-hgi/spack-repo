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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/CopyhelpeR_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/CopyhelpeR/CopyhelpeR_1.34.0.tar.gz"]

	version("1.34.0", sha256="305c890df69d08425b48b02467b723abd1becf7dced083961bc9525a4cecdafd")

	depends_on("r@3.5:", type=("build", "run"))

