# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeBtaurusUcscBostau6(RPackage):
	"""Full genome sequences for Bos taurus (UCSC version bosTau6)

	Full genome sequences for Bos taurus (Cow) as provided by UCSC (bosTau6, Nov. 2009) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Btaurus.UCSC.bosTau6" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Btaurus.UCSC.bosTau6_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Btaurus.UCSC.bosTau6/BSgenome.Btaurus.UCSC.bosTau6_1.4.0.tar.gz"]

	version("1.4.0", md5="b22391e0678fc3743daa4b77ecc55f66", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Btaurus.UCSC.bosTau6_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation