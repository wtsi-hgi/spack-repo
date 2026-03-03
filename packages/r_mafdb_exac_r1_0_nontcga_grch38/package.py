# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMafdbExacR10NontcgaGrch38(RPackage):
	"""Minor allele frequency data from ExAC release 1.0 subset of nonTCGA exomes for GRCh38

	Store minor allele frequency data from the Exome Aggregation Consortium (ExAC release 1.0 subset of nonTCGA exomes) for the human genome version GRCh38.
	"""
	
	bioc = "MafDb.ExAC.r1.0.nonTCGA.GRCh38" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/MafDb.ExAC.r1.0.nonTCGA.GRCh38_3.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/MafDb.ExAC.r1.0.nonTCGA.GRCh38/MafDb.ExAC.r1.0.nonTCGA.GRCh38_3.10.0.tar.gz"]

	version("3.10.0", md5="cf447f59cc8b1cd7ca395fd3fe6e4730", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/MafDb.ExAC.r1.0.nonTCGA.GRCh38_3.10.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicscores@1.9.6:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

