# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbHsapiensUcscHg38Knowngene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Hsapiens.UCSC.hg38.knownGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Hsapiens.UCSC.hg38.knownGene_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Hsapiens.UCSC.hg38.knownGene/TxDb.Hsapiens.UCSC.hg38.knownGene_3.18.0.tar.gz"]

	version("3.18.0", sha256="a509363b19906d67e45712f28e32f0423b7a889ec0d83b5555b2094a2553662a")

	depends_on("r-genomicfeatures@1.53.2:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

