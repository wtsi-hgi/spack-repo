# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbPtroglodytesUcscPantro4Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Ptroglodytes.UCSC.panTro4.refGene" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Ptroglodytes.UCSC.panTro4.refGene_3.12.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Ptroglodytes.UCSC.panTro4.refGene/TxDb.Ptroglodytes.UCSC.panTro4.refGene_3.12.0.tar.gz"]

	version("3.12.0", md5="9bdd3ba81561550f50250368d7d52eaa")

	depends_on("r-genomicfeatures@1.41.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation