# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbMmusculusUcscMm9Knowngene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Mmusculus.UCSC.mm9.knownGene" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Mmusculus.UCSC.mm9.knownGene_3.2.2.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Mmusculus.UCSC.mm9.knownGene/TxDb.Mmusculus.UCSC.mm9.knownGene_3.2.2.tar.gz"]

	version("3.2.2", md5="cb72af039b011033477363bda8ed9104")

	depends_on("r-genomicfeatures@1.21.30:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation