# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbDmelanogasterUcscDm3Ensgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Dmelanogaster.UCSC.dm3.ensGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Dmelanogaster.UCSC.dm3.ensGene_3.2.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Dmelanogaster.UCSC.dm3.ensGene/TxDb.Dmelanogaster.UCSC.dm3.ensGene_3.2.2.tar.gz"]

	version("3.2.2", sha256="879d366e7c6ca9734a059c060e0b36019e11f32c42e83a90fa31d69687e8678c")

	depends_on("r-genomicfeatures@1.21.30:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

