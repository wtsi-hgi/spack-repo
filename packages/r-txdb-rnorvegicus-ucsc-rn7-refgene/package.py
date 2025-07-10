# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbRnorvegicusUcscRn7Refgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Rnorvegicus.UCSC.rn7.refGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Rnorvegicus.UCSC.rn7.refGene_3.15.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Rnorvegicus.UCSC.rn7.refGene/TxDb.Rnorvegicus.UCSC.rn7.refGene_3.15.0.tar.gz"]

	version("3.15.0", sha256="8ea4f1850d07358bd149e862a1489bda40e59f8d2d6b12eccb9d53a603197f6f")

	depends_on("r-genomicfeatures@1.47.13:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

