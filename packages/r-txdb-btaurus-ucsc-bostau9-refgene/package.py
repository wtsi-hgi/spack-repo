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

	version("3.10.0", md5="fe443d123b0b788e1e450f4e60036788")

	depends_on("r-genomicfeatures@1.37.6:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation