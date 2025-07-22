# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbRnorvegicusUcscRn5Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Rnorvegicus.UCSC.rn5.refGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Rnorvegicus.UCSC.rn5.refGene_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Rnorvegicus.UCSC.rn5.refGene/TxDb.Rnorvegicus.UCSC.rn5.refGene_3.12.0.tar.gz"]

	version("3.12.0", sha256="f10bbf742f85c4188890cb40191c58e2880ec2c5ea2246c15fccc5ddea4c6e22")

	depends_on("r-genomicfeatures@1.41.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

