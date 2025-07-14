# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROligo(RPackage):
	"""Preprocessing tools for oligonucleotide arrays

	A package to analyze oligonucleotide arrays (expression/SNP/tiling/exon) at probe-level. It currently supports Affymetrix (CEL files) and NimbleGen arrays (XYS files).
	"""
	
	bioc = "oligo"

	version("1.72.0", commit="bced0213e184e46e77e8ef639f334435ded5f8f2")
	version("1.66.0", commit="e6e72834cb549bc519cdf0a8c6cb3de13e8ec851")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.11:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-biobase@2.27.3:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-affyio@1.35:", type=("build", "run"))
	depends_on("r-affxparser@1.39.4:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
