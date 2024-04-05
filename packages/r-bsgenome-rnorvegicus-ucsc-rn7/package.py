# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeRnorvegicusUcscRn7(RPackage):
	"""Full genome sequences for Rattus norvegicus (UCSC genome rn7)

	Full genome sequences for Rattus norvegicus (Rat) as provided by UCSC (genome rn7) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Rnorvegicus.UCSC.rn7" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn7_1.4.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Rnorvegicus.UCSC.rn7/BSgenome.Rnorvegicus.UCSC.rn7_1.4.3.tar.gz"]

	version("1.4.3", md5="c64f7dd9e30ff88ce02ecd3712e4c454", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn7_1.4.3.tar.gz")
	version("1.4.3", md5="c64f7dd9e30ff88ce02ecd3712e4c454", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn7_1.4.3.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

