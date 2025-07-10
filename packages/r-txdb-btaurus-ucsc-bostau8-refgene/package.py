# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbBtaurusUcscBostau8Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Btaurus.UCSC.bosTau8.refGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Btaurus.UCSC.bosTau8.refGene_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Btaurus.UCSC.bosTau8.refGene/TxDb.Btaurus.UCSC.bosTau8.refGene_3.12.0.tar.gz"]

	version("3.12.0", sha256="2c0148538a2d2fda1762350f8cb9a179669326af5cfa30ecec88d33125b906cc")

	depends_on("r-genomicfeatures@1.41.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

