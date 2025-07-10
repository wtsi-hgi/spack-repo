# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbCelegansUcscCe6Ensgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Celegans.UCSC.ce6.ensGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Celegans.UCSC.ce6.ensGene_3.2.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Celegans.UCSC.ce6.ensGene/TxDb.Celegans.UCSC.ce6.ensGene_3.2.2.tar.gz"]

	version("3.2.2", sha256="20c51a06664f1135500b3ce1b9eeacf5154995ab4847217524beb131d4bef7e9")

	depends_on("r-genomicfeatures@1.21.30:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

