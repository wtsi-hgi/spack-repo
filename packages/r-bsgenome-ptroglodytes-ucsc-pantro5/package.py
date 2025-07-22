# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomePtroglodytesUcscPantro5(RPackage):
	"""Full genome sequences for Pan troglodytes (UCSC version panTro5)

	Full genome sequences for Pan troglodytes (Chimp) as provided by UCSC (panTro5, May 2016) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Ptroglodytes.UCSC.panTro5" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro5_1.4.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ptroglodytes.UCSC.panTro5/BSgenome.Ptroglodytes.UCSC.panTro5_1.4.2.tar.gz"]

	version("1.4.2", sha256="bab1574aff7dcb15e5e865dbcdafb616852a8b0851b26f9ec91038cfa48aac73", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro5_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

