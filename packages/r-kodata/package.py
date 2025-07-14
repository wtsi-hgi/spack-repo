# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKodata(RPackage):
	"""LINCS Knock-Out Data Package

	Contains consensus genomic signatures (CGS) for experimental cell-line specific gene knock-outs as well as baseline gene expression data for a subset of experimental cell-lines. Intended for use with package KEGGlincs.
	"""
	
	bioc = "KOdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/KOdata_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/KOdata/KOdata_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="8a4aa27165cf43268fa9e9a1aed2cf18659558459d130d8c864ab0f3ddd6d4b5")

	depends_on("r@3.3:", type=("build", "run"))

