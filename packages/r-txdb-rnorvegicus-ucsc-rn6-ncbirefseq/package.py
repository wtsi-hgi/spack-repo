# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbRnorvegicusUcscRn6Ncbirefseq(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Rnorvegicus.UCSC.rn6.ncbiRefSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Rnorvegicus.UCSC.rn6.ncbiRefSeq_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Rnorvegicus.UCSC.rn6.ncbiRefSeq/TxDb.Rnorvegicus.UCSC.rn6.ncbiRefSeq_3.12.0.tar.gz"]

	version("3.12.0", sha256="dc977fb0b92300e8b2fef183597213fe8206559b646f8872603ef6f011a268bd")

	depends_on("r-genomicfeatures@1.41.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

