# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbPtroglodytesUcscPantro6Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Ptroglodytes.UCSC.panTro6.refGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Ptroglodytes.UCSC.panTro6.refGene_3.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Ptroglodytes.UCSC.panTro6.refGene/TxDb.Ptroglodytes.UCSC.panTro6.refGene_3.10.0.tar.gz"]

	version("3.10.0", sha256="eac7feb705086352fae0b3f317db90596282735db9fe24baed7322e2f9c1947c")

	depends_on("r-genomicfeatures@1.37.6:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

