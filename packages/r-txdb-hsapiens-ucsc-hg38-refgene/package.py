# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbHsapiensUcscHg38Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Hsapiens.UCSC.hg38.refGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Hsapiens.UCSC.hg38.refGene_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Hsapiens.UCSC.hg38.refGene/TxDb.Hsapiens.UCSC.hg38.refGene_3.18.0.tar.gz"]

	version("3.18.0", md5="7ec982095ea795b99d53b6549d7ba4d4")

	depends_on("r-genomicfeatures@1.53.2:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation