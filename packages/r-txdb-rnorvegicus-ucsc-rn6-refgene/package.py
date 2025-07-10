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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Rnorvegicus.UCSC.rn6.refGene_3.4.6.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Rnorvegicus.UCSC.rn6.refGene/TxDb.Rnorvegicus.UCSC.rn6.refGene_3.4.6.tar.gz"]

	version("3.4.6", sha256="9927fd7695806d5abdc3e2c29b4faf1955a8ad8c95221d131279e0c641a438de")

	depends_on("r-genomicfeatures@1.35.11:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

