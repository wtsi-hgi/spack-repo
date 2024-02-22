# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbHsapiensUcscHg18Knowngene(RPackage):
	"""Annotation package for TxDb object(s).

	Exposes an annotation databases generated from UCSC by exposing these as
	TxDb objects"""

	# This is a bioconductor package but ther is no available git repo
	bioc = "TxDb.Hsapiens.UCSC.hg18.knownGene"
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Hsapiens.UCSC.hg18.knownGene_3.2.2.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Hsapiens.UCSC.hg18.knownGene/TxDb.Hsapiens.UCSC.hg18.knownGene_3.2.2.tar.gz"]

	version("3.2.2", md5="e8b32a672e87345c72bb30be73d1e2d6")

	depends_on("r-genomicfeatures@1.21.30:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation