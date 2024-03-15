# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpitxdbScSaccer3(RPackage):
	"""Annotation package for EpiTxDb objects

	Exposes an annotation databases generated from several sources by exposing these as EpiTxDb object. Generated for Saccharomyces cerevisiae/sacCer3.
	"""
	
	homepage = "https://github.com/FelixErnst/EpiTxDb.Sc.sacCer3"
	bioc = "EpiTxDb.Sc.sacCer3" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EpiTxDb.Sc.sacCer3_0.99.5.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/EpiTxDb.Sc.sacCer3/EpiTxDb.Sc.sacCer3_0.99.5.tar.gz"]

	version("0.99.5", md5="6d9e5f37e5dcb60e890d99d80fddda00", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EpiTxDb.Sc.sacCer3_0.99.5.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-epitxdb", type=("build", "run"))

	# annotation