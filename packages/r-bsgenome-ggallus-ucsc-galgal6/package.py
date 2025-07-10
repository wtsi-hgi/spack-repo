# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeGgallusUcscGalgal6(RPackage):
	"""Full genome sequences for Gallus gallus (UCSC version galGal6)

	Full genome sequences for Gallus gallus (Chicken) as provided by UCSC (galGal6, Mar. 2018) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Ggallus.UCSC.galGal6" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ggallus.UCSC.galGal6_1.4.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ggallus.UCSC.galGal6/BSgenome.Ggallus.UCSC.galGal6_1.4.2.tar.gz"]

	version("1.4.2", sha256="629f89de5c48007e3591f00c65865bb2bce93580a1a7bdb574b3971127576001", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ggallus.UCSC.galGal6_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

