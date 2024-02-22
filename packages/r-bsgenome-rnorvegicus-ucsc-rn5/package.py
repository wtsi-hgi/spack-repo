# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeRnorvegicusUcscRn5(RPackage):
	"""Full genome sequences for Rattus norvegicus (UCSC version rn5)

	Full genome sequences for Rattus norvegicus (Rat) as provided by UCSC (rn5, Mar. 2012) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Rnorvegicus.UCSC.rn5" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn5_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Rnorvegicus.UCSC.rn5/BSgenome.Rnorvegicus.UCSC.rn5_1.4.0.tar.gz"]

	version("1.4.0", md5="723b1f3ced395ef638b2d68053b05c86", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn5_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation