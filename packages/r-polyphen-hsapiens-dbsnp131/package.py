# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolyphenHsapiensDbsnp131(RPackage):
	"""PolyPhen Predictions for Homo sapiens dbSNP build 131

	Database of PolyPhen predictions for Homo sapiens dbSNP build 131
	"""
	
	bioc = "PolyPhen.Hsapiens.dbSNP131" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/PolyPhen.Hsapiens.dbSNP131_1.0.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/PolyPhen.Hsapiens.dbSNP131/PolyPhen.Hsapiens.dbSNP131_1.0.2.tar.gz"]

	version("1.0.2", md5="763e9cd4afd97b36f7e659f5454ef61f", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/PolyPhen.Hsapiens.dbSNP131_1.0.2.tar.gz")

	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-rsqlite@0.11:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

