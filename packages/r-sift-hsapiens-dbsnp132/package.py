# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiftHsapiensDbsnp132(RPackage):
	"""SIFT Predictions for Homo sapiens dbSNP build 132

	Database of SIFT predictions for Homo sapiens dbSNP build 132
	"""
	
	bioc = "SIFT.Hsapiens.dbSNP132" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SIFT.Hsapiens.dbSNP132_1.0.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/SIFT.Hsapiens.dbSNP132/SIFT.Hsapiens.dbSNP132_1.0.2.tar.gz"]

	version("1.0.2", md5="c374f0bf4c99357cfe99e0b192c00d75", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SIFT.Hsapiens.dbSNP132_1.0.2.tar.gz")

	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-rsqlite@0.11:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation