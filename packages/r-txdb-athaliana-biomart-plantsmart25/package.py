# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbAthalianaBiomartPlantsmart25(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from BioMart by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Athaliana.BioMart.plantsmart25" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Athaliana.BioMart.plantsmart25_3.1.3.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/TxDb.Athaliana.BioMart.plantsmart25/TxDb.Athaliana.BioMart.plantsmart25_3.1.3.tar.gz"]

	version("3.1.3", md5="eb007c07317b9717c76949e5ed999978", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Athaliana.BioMart.plantsmart25_3.1.3.tar.gz")

	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation