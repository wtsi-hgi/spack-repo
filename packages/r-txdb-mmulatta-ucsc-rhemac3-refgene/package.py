# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbMmulattaUcscRhemac3Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Mmulatta.UCSC.rheMac3.refGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Mmulatta.UCSC.rheMac3.refGene_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Mmulatta.UCSC.rheMac3.refGene/TxDb.Mmulatta.UCSC.rheMac3.refGene_3.12.0.tar.gz"]

	version("3.12.0", sha256="077001ff7f84268c2bb7183a0626fd745a33d0dd8b47c1abf5ef4ad5085c1ca8")

	depends_on("r-genomicfeatures@1.41.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

