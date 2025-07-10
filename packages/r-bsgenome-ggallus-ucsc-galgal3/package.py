# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeGgallusUcscGalgal3(RPackage):
	"""Full genome sequences for Gallus gallus (UCSC version galGal3)

	Full genome sequences for Gallus gallus (Chicken) as provided by UCSC (galGal3, May 2006) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Ggallus.UCSC.galGal3" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ggallus.UCSC.galGal3_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ggallus.UCSC.galGal3/BSgenome.Ggallus.UCSC.galGal3_1.4.0.tar.gz"]

	version("1.4.0", sha256="5747f2ae9401ef0d2f39450c9ceb459505e327c95a1161009ea1b61f6d21fcad", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ggallus.UCSC.galGal3_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

