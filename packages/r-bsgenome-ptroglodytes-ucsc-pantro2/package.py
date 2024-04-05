# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomePtroglodytesUcscPantro2(RPackage):
	"""Full genome sequences for Pan troglodytes (UCSC version panTro2)

	Full genome sequences for Pan troglodytes (Chimp) as provided by UCSC (panTro2, Mar. 2006) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Ptroglodytes.UCSC.panTro2" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro2_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ptroglodytes.UCSC.panTro2/BSgenome.Ptroglodytes.UCSC.panTro2_1.4.0.tar.gz"]

	version("1.4.0", md5="780200c315779ac75fcf0bdeb9a2eb8c", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro2_1.4.0.tar.gz")
	version("1.4.0", md5="780200c315779ac75fcf0bdeb9a2eb8c", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro2_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

