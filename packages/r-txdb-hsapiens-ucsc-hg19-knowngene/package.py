# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbHsapiensUcscHg19Knowngene(RPackage):
	"""Annotation package for TxDb object(s).

	Exposes an annotation databases generated from UCSC by exposing these as
	TxDb objects."""

	# This is a bioconductor package but there is no available git repo.
	bioc = "TxDb.Hsapiens.UCSC.hg19.knownGene"
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Hsapiens.UCSC.hg19.knownGene_3.2.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Hsapiens.UCSC.hg19.knownGene/TxDb.Hsapiens.UCSC.hg19.knownGene_3.2.2.tar.gz"]
	
	version("3.2.2", md5="61be88a81433958571b57d0952be48a0")

	depends_on("r-genomicfeatures@1.21.30:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation