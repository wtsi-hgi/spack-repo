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

	version("3.18.0", sha256="7986a7c56814f7252724d04ae2c886e89b0ea5fb92bbad2e4fd1be019a538e0f")

	depends_on("r-genomicfeatures@1.53.2:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

