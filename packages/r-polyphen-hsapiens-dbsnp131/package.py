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

	version("1.0.2", sha256="ecb8092a63f8a8f0ea4e42ba488c100fd77c8948e0c388f3b03a9048e7f333ce", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/PolyPhen.Hsapiens.dbSNP131_1.0.2.tar.gz")

	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-rsqlite@0.11:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

