# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbRnorvegicusUcscRn4Ensgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Rnorvegicus.UCSC.rn4.ensGene" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Rnorvegicus.UCSC.rn4.ensGene_3.2.2.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Rnorvegicus.UCSC.rn4.ensGene/TxDb.Rnorvegicus.UCSC.rn4.ensGene_3.2.2.tar.gz"]

	version("3.2.2", md5="6bf2ebc522c2828c036e52b2028792c1")

	depends_on("r-genomicfeatures@1.21.30:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation