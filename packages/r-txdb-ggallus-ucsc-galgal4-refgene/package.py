# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbGgallusUcscGalgal4Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Ggallus.UCSC.galGal4.refGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Ggallus.UCSC.galGal4.refGene_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Ggallus.UCSC.galGal4.refGene/TxDb.Ggallus.UCSC.galGal4.refGene_3.12.0.tar.gz"]

	version("3.12.0", sha256="a50a8c97d195c986ca062c7cce10b1a1abca69cd0726e9a0efec9f0ef1d63531")

	depends_on("r-genomicfeatures@1.41.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

