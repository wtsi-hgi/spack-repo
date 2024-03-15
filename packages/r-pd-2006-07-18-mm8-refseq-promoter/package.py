# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPd20060718Mm8RefseqPromoter(RPackage):
	"""Platform Design Info for NimbleGen 2006-07-18_mm8_refseq_promoter

	Platform Design Info for NimbleGen 2006-07-18_mm8_refseq_promoter
	"""
	
	bioc = "pd.2006.07.18.mm8.refseq.promoter" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.2006.07.18.mm8.refseq.promoter_0.99.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.2006.07.18.mm8.refseq.promoter/pd.2006.07.18.mm8.refseq.promoter_0.99.3.tar.gz"]

	version("0.99.3", md5="084b0a6759fd96d1bc775dd4c66c42b0")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-rsqlite@0.7.1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.9.30:", type=("build", "run"))
	depends_on("r-oligo@1.11.18:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-biostrings@2.13.50:", type=("build", "run"))
	depends_on("r-iranges@1.3.89:", type=("build", "run"))

	# annotation