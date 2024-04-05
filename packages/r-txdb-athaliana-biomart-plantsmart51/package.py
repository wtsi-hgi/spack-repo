# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbAthalianaBiomartPlantsmart51(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from BioMart by exposing these as TxDb objects. This package is for Arabidopsis thaliana (taxID: 3702). The BioMart plantsmart release number is 51.
	"""
	
	bioc = "TxDb.Athaliana.BioMart.plantsmart51" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Athaliana.BioMart.plantsmart51_0.99.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Athaliana.BioMart.plantsmart51/TxDb.Athaliana.BioMart.plantsmart51_0.99.0.tar.gz"]

	version("0.99.0", md5="c623af555537bfd9958f8f9573308103", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/TxDb.Athaliana.BioMart.plantsmart51_0.99.0.tar.gz")
	version("0.99.0", md5="c623af555537bfd9958f8f9573308103", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Athaliana.BioMart.plantsmart51_0.99.0.tar.gz")

	depends_on("r-genomicfeatures@1.45:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

