# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbBtaurusUcscBostau9Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Btaurus.UCSC.bosTau9.refGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Btaurus.UCSC.bosTau9.refGene_3.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Btaurus.UCSC.bosTau9.refGene/TxDb.Btaurus.UCSC.bosTau9.refGene_3.10.0.tar.gz"]

	version("3.10.0", sha256="099319772d95999f63318f78e23dc536a107fe35321a2997dac206a9944cf8ec")

	depends_on("r-genomicfeatures@1.37.6:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

