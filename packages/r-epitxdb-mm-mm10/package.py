# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpitxdbMmMm10(RPackage):
	"""Annotation package for EpiTxDb objects

	Exposes an annotation databases generated from several sources by exposing these as EpiTxDb object. Generated for Mus musculus/mm10.
	"""
	
	homepage = "https://github.com/FelixErnst/EpiTxDb.Mm.mm10"
	bioc = "EpiTxDb.Mm.mm10" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EpiTxDb.Mm.mm10_0.99.6.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/EpiTxDb.Mm.mm10/EpiTxDb.Mm.mm10_0.99.6.tar.gz"]

    version("0.99.6", tag="RELEASE_3_21")
	version("0.99.6", sha256="9c5fe8bde6fea90f9c84721d1b8398205d88fbac18568735d8fcfab1b2c5fa9b", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EpiTxDb.Mm.mm10_0.99.6.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-epitxdb", type=("build", "run"))

