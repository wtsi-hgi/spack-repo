# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpitxdbHsHg38(RPackage):
	"""Annotation package for EpiTxDb objects

	Exposes an annotation databases generated from several sources by exposing these as EpiTxDb object. Generated for Homo sapiens/hg38.
	"""
	
	homepage = "https://github.com/FelixErnst/EpiTxDb.Hs.hg38"
	bioc = "EpiTxDb.Hs.hg38" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EpiTxDb.Hs.hg38_0.99.7.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/EpiTxDb.Hs.hg38/EpiTxDb.Hs.hg38_0.99.7.tar.gz"]

    version("0.99.7", tag="RELEASE_3_21")
	version("0.99.7", sha256="cedbed7a0e76b95e77ebdedfca0af4c48ed207d013a2db97a5980b90301151ef", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EpiTxDb.Hs.hg38_0.99.7.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-epitxdb", type=("build", "run"))

