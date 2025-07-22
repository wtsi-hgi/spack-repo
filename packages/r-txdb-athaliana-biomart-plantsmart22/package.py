# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbAthalianaBiomartPlantsmart22(RPackage):
	"""Annotation package for TxDb object(s)

	Exposes an annotation databases generated from BioMart by exposing these as TxDb objects
	"""
	
	bioc = "TxDb.Athaliana.BioMart.plantsmart22" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Athaliana.BioMart.plantsmart22_3.0.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/TxDb.Athaliana.BioMart.plantsmart22/TxDb.Athaliana.BioMart.plantsmart22_3.0.1.tar.gz"]

	version("3.0.1", sha256="ecdfdce350318df62292695ebaac944a1eef9f9ba9a6de69f8a7a9d618c95f48", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/TxDb.Athaliana.BioMart.plantsmart22_3.0.1.tar.gz")

	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

