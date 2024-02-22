# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbMmusculusUcscMm39Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Mmusculus.UCSC.mm39.refGene" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Mmusculus.UCSC.mm39.refGene_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Mmusculus.UCSC.mm39.refGene/TxDb.Mmusculus.UCSC.mm39.refGene_3.18.0.tar.gz"]

	version("3.18.0", md5="2fd64557d5f1bade11432b666c63f33a")

	depends_on("r-genomicfeatures@1.53.2:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation