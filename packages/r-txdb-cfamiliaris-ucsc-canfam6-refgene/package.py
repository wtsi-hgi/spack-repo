# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbCfamiliarisUcscCanfam6Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Cfamiliaris.UCSC.canFam6.refGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Cfamiliaris.UCSC.canFam6.refGene_3.17.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Cfamiliaris.UCSC.canFam6.refGene/TxDb.Cfamiliaris.UCSC.canFam6.refGene_3.17.0.tar.gz"]

	version("3.17.0", md5="9279204329323191fbb72717a57b13aa")

	depends_on("r-genomicfeatures@1.51.4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation