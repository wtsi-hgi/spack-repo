# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdbInfiniummethylationHg18(RPackage):
	"""Annotation package for Illumina Infinium DNA methylation probes.

	Compiled HumanMethylation27 and HumanMethylation450 annotations"""

	# This is a bioconductor package but there is no available git repository
	bioc = "FDb.InfiniumMethylation.hg18"
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/FDb.InfiniumMethylation.hg18_2.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/FDb.InfiniumMethylation.hg18/FDb.InfiniumMethylation.hg18_2.2.0.tar.gz"]
	
	version("2.2.0", sha256="4a9028ac03c11fffbab731ea750bc7f9b0884fc43c6a8dac6eb2c644e4c79f6f", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/FDb.InfiniumMethylation.hg18_2.2.0.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg18-knowngene", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))

