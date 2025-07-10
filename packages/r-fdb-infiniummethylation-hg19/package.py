# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdbInfiniummethylationHg19(RPackage):
	"""Annotation package for Illumina Infinium DNA methylation probes.

	Compiled HumanMethylation27 and HumanMethylation450 annotations."""

	# No available git repository
	bioc = "FDb.InfiniumMethylation.hg19"
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/FDb.InfiniumMethylation.hg19_2.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/FDb.InfiniumMethylation.hg19/FDb.InfiniumMethylation.hg19_2.2.0.tar.gz"]
	
	version("2.2.0", sha256="605aa3643588a2f40a942fa760b92662060a0dfedb26b4e4cd6f1a78b703093f", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/FDb.InfiniumMethylation.hg19_2.2.0.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))

