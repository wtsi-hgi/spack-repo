# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomePpaniscusUcscPanpan2(RPackage):
	"""Full genome sequences for Pan paniscus (UCSC version panPan2)

	Full genome sequences for Pan paniscus (Bonobo) as provided by UCSC (panPan2, Dec. 2015) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Ppaniscus.UCSC.panPan2" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ppaniscus.UCSC.panPan2_1.4.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ppaniscus.UCSC.panPan2/BSgenome.Ppaniscus.UCSC.panPan2_1.4.3.tar.gz"]

	version("1.4.3", md5="74973376a6377d6820d6cd7fb3655a19", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Ppaniscus.UCSC.panPan2_1.4.3.tar.gz")
	version("1.4.3", md5="74973376a6377d6820d6cd7fb3655a19", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ppaniscus.UCSC.panPan2_1.4.3.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

