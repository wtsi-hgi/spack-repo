# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbHsapiensBiomartIgis(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from BioMart by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Hsapiens.BioMart.igis" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Hsapiens.BioMart.igis_2.3.2.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Hsapiens.BioMart.igis/TxDb.Hsapiens.BioMart.igis_2.3.2.tar.gz"]

	version("2.3.2", md5="75b793928d29bcd3f069b5986bc2cfae")

	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation