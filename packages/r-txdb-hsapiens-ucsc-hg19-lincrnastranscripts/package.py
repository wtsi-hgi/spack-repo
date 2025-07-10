# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbHsapiensUcscHg19Lincrnastranscripts(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Hsapiens.UCSC.hg19.lincRNAsTranscripts" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Hsapiens.UCSC.hg19.lincRNAsTranscripts_3.2.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Hsapiens.UCSC.hg19.lincRNAsTranscripts/TxDb.Hsapiens.UCSC.hg19.lincRNAsTranscripts_3.2.2.tar.gz"]

	version("3.2.2", sha256="4f68ee75c1722b53de4a5382a455730673dab8c0fd7585f86771efe6e7b9ab2e")

	depends_on("r-genomicfeatures@1.21.30:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

