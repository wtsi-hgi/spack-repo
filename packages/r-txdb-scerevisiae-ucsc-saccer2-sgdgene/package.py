# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbScerevisiaeUcscSaccer2Sgdgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Scerevisiae.UCSC.sacCer2.sgdGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Scerevisiae.UCSC.sacCer2.sgdGene_3.2.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Scerevisiae.UCSC.sacCer2.sgdGene/TxDb.Scerevisiae.UCSC.sacCer2.sgdGene_3.2.2.tar.gz"]

	version("3.2.2", sha256="eaf35b5a3e4706328e7a5b89d7de846055f5ac0aa34109d305a6ffbd2067af50")

	depends_on("r-genomicfeatures@1.21.30:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

