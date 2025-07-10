# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbSscrofaUcscSusscr3Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Sscrofa.UCSC.susScr3.refGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Sscrofa.UCSC.susScr3.refGene_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Sscrofa.UCSC.susScr3.refGene/TxDb.Sscrofa.UCSC.susScr3.refGene_3.12.0.tar.gz"]

	version("3.12.0", sha256="d7b0aff9bf2e5066d5027d643f7b8c3901edc211274269c0210f42dfdb3f7405")

	depends_on("r-genomicfeatures@1.41.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

