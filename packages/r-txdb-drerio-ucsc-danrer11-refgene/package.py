# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbDrerioUcscDanrer11Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Drerio.UCSC.danRer11.refGene" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Drerio.UCSC.danRer11.refGene_3.4.6.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Drerio.UCSC.danRer11.refGene/TxDb.Drerio.UCSC.danRer11.refGene_3.4.6.tar.gz"]

	version("3.4.6", md5="3d4ded4cec068a807b8b86b31389b677")

	depends_on("r-genomicfeatures@1.35.11:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation