# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhastcons7wayUcscHg38(RPackage):
	"""UCSC phastCons conservation scores for hg38

	Store UCSC phastCons conservation scores for the human genome (hg38) calculated from multiple alignments with other 6 vertebrate species.
	"""
	
	bioc = "phastCons7way.UCSC.hg38" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/phastCons7way.UCSC.hg38_3.7.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/phastCons7way.UCSC.hg38/phastCons7way.UCSC.hg38_3.7.1.tar.gz"]

	version("3.7.1", md5="c2d87446b022c166c1c325ea2aef521d", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/phastCons7way.UCSC.hg38_3.7.1.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-genomicscores@1.3.19:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

