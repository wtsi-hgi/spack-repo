# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeBtaurusUcscBostau8(RPackage):
	"""Full genome sequences for Bos taurus (UCSC version bosTau8)

	Full genome sequences for Bos taurus (Cow) as provided by UCSC (bosTau8, Jun. 2014) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Btaurus.UCSC.bosTau8" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Btaurus.UCSC.bosTau8_1.4.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Btaurus.UCSC.bosTau8/BSgenome.Btaurus.UCSC.bosTau8_1.4.2.tar.gz"]

	version("1.4.2", sha256="e66bdab1b7d650240eb0a07d665344f60eae0f2fd0237ef2007ddbc455f0929b", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Btaurus.UCSC.bosTau8_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

