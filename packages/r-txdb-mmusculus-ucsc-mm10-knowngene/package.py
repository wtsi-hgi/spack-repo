# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbMmusculusUcscMm10Knowngene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Mmusculus.UCSC.mm10.knownGene" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Mmusculus.UCSC.mm10.knownGene_3.10.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Mmusculus.UCSC.mm10.knownGene/TxDb.Mmusculus.UCSC.mm10.knownGene_3.10.0.tar.gz"]

	version("3.10.0", md5="129b610bf05ec77451731196baa55bcc")

	depends_on("r-genomicfeatures@1.37.4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation