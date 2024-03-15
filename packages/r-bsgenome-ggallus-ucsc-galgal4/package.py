# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeGgallusUcscGalgal4(RPackage):
	"""Full genome sequences for Gallus gallus (UCSC version galGal4)

	Full genome sequences for Gallus gallus (Chicken) as provided by UCSC (galGal4, Nov. 2011) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Ggallus.UCSC.galGal4" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ggallus.UCSC.galGal4_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ggallus.UCSC.galGal4/BSgenome.Ggallus.UCSC.galGal4_1.4.0.tar.gz"]

	version("1.4.0", md5="c2cb4bfc39db93c060e78d8d12542c11", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ggallus.UCSC.galGal4_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation