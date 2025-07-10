# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbMmusculusUcscMm39Knowngene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Mmusculus.UCSC.mm39.knownGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Mmusculus.UCSC.mm39.knownGene_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Mmusculus.UCSC.mm39.knownGene/TxDb.Mmusculus.UCSC.mm39.knownGene_3.18.0.tar.gz"]

	version("3.18.0", sha256="6a6b6f598a688aa4c85ffc31493b49f1c6c079e71b324990f9ba04dc9a773918")

	depends_on("r-genomicfeatures@1.53.2:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

