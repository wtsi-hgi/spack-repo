# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMdomesticaUcscMondom5(RPackage):
	"""Full genome sequences for Monodelphis domestica (UCSC version monDom5)

	Full genome sequences for Monodelphis domestica (Opossum) as provided by UCSC (monDom5, Oct. 2006) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Mdomestica.UCSC.monDom5" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mdomestica.UCSC.monDom5_1.4.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mdomestica.UCSC.monDom5/BSgenome.Mdomestica.UCSC.monDom5_1.4.2.tar.gz"]

	version("1.4.2", md5="ff940f7446a275962f69a6f4cb84724c", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mdomestica.UCSC.monDom5_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

