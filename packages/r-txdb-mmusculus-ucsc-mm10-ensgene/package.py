# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbMmusculusUcscMm10Ensgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Mmusculus.UCSC.mm10.ensGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Mmusculus.UCSC.mm10.ensGene_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Mmusculus.UCSC.mm10.ensGene/TxDb.Mmusculus.UCSC.mm10.ensGene_3.4.0.tar.gz"]

	version("3.4.0", md5="88d65b714d1f86b456aee2b8524e9d84")

	depends_on("r-genomicfeatures@1.25.17:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation