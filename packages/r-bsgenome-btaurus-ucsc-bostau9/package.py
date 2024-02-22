# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeBtaurusUcscBostau9(RPackage):
	"""Full genome sequences for Bos taurus (UCSC version bosTau9)

	Full genome sequences for Bos taurus (Cow) as provided by UCSC (bosTau9, Apr. 2018) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Btaurus.UCSC.bosTau9" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Btaurus.UCSC.bosTau9_1.4.2.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Btaurus.UCSC.bosTau9/BSgenome.Btaurus.UCSC.bosTau9_1.4.2.tar.gz"]

	version("1.4.2", md5="9b3343725d85c093999413d91218079d", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Btaurus.UCSC.bosTau9_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation