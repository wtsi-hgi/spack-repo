# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbCfamiliarisUcscCanfam3Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Cfamiliaris.UCSC.canFam3.refGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Cfamiliaris.UCSC.canFam3.refGene_3.11.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Cfamiliaris.UCSC.canFam3.refGene/TxDb.Cfamiliaris.UCSC.canFam3.refGene_3.11.0.tar.gz"]

	version("3.11.0", sha256="79169a3d0b1797b2c0af73f550c0a52e68448144298c24b36b63756c5bf32f66")

	depends_on("r-genomicfeatures@1.39.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

