# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitconsUcscHg19(RPackage):
	"""UCSC fitCons fitness consequences scores for hg19

	Store UCSC fitCons fitness consequences scores version 1.01 for the human genome (hg19).
	"""
	
	bioc = "fitCons.UCSC.hg19" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/fitCons.UCSC.hg19_3.7.1.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/fitCons.UCSC.hg19/fitCons.UCSC.hg19_3.7.1.tar.gz"]

	version("3.7.1", md5="53d954890ec9b91084664a10161ce391", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/fitCons.UCSC.hg19_3.7.1.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-genomicscores@1.3.19:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

	# annotation