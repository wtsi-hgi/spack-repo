# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbCelegansUcscCe11Ensgene(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from UCSC by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Celegans.UCSC.ce11.ensGene" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Celegans.UCSC.ce11.ensGene_3.15.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Celegans.UCSC.ce11.ensGene/TxDb.Celegans.UCSC.ce11.ensGene_3.15.0.tar.gz"]

	version("3.15.0", sha256="71018eaeec458639aacc9543da764d2c0e34497fc075cb2d44e801b64872215f")

	depends_on("r-genomicfeatures@1.47.13:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

