# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPd20060718Hg18RefseqPromoter(RPackage):
	"""Platform Design Info for NimbleGen 2006-07-18_hg18_refseq_promoter

	Platform Design Info for NimbleGen 2006-07-18_hg18_refseq_promoter
	"""
	
	bioc = "pd.2006.07.18.hg18.refseq.promoter" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.2006.07.18.hg18.refseq.promoter_1.8.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.2006.07.18.hg18.refseq.promoter/pd.2006.07.18.hg18.refseq.promoter_1.8.1.tar.gz"]

	version("1.8.1", md5="00838332d75b82d212078a9957f495df")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rsqlite@0.11.1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.19.41:", type=("build", "run"))
	depends_on("r-oligo@1.21.5:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-biostrings@2.25.12:", type=("build", "run"))
	depends_on("r-iranges@1.15.43:", type=("build", "run"))

	# annotation