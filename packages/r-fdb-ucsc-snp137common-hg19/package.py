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

	version("1.0.0", md5="dac83f2d2f9ea9f033e50beac5c44838", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/FDb.UCSC.snp137common.hg19_1.0.0.tar.gz")

	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation