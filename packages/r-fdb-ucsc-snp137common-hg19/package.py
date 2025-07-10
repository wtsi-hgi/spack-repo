# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdbUcscSnp137commonHg19(RPackage):
	"""UCSC common SNPs track for dbSNP build 137

	makeFeatureDbFromUCSC cannot cope with this track, hence a package
	"""
	
	bioc = "FDb.UCSC.snp137common.hg19" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/FDb.UCSC.snp137common.hg19_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/FDb.UCSC.snp137common.hg19/FDb.UCSC.snp137common.hg19_1.0.0.tar.gz"]

	version("1.0.0", sha256="c3603146f17a923f9c75106eb87fe726522767f06e3bf3fba71fe024663e39e0", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/FDb.UCSC.snp137common.hg19_1.0.0.tar.gz")

	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

