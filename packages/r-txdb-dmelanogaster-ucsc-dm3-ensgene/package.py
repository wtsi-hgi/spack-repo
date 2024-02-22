# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbDmelanogasterUcscDm3Ensgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Dmelanogaster.UCSC.dm3.ensGene" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Dmelanogaster.UCSC.dm3.ensGene_3.2.2.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Dmelanogaster.UCSC.dm3.ensGene/TxDb.Dmelanogaster.UCSC.dm3.ensGene_3.2.2.tar.gz"]

	version("3.2.2", md5="46b7ffe0c516edf8a2a3b5d78e0d8b67")

	depends_on("r-genomicfeatures@1.21.30:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation