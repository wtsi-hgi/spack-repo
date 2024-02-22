# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbRnorvegicusUcscRn6Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Rnorvegicus.UCSC.rn6.refGene" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Rnorvegicus.UCSC.rn6.refGene_3.4.6.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Rnorvegicus.UCSC.rn6.refGene/TxDb.Rnorvegicus.UCSC.rn6.refGene_3.4.6.tar.gz"]

	version("3.4.6", md5="ea525daa75bcf165eb24f6e93f4dbf6c")

	depends_on("r-genomicfeatures@1.35.11:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation