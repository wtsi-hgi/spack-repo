# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomePtroglodytesUcscPantro3(RPackage):
	"""Full genome sequences for Pan troglodytes (UCSC version panTro3)

	Full genome sequences for Pan troglodytes (Chimp) as provided by UCSC (panTro3, Oct. 2010) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Ptroglodytes.UCSC.panTro3" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro3_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ptroglodytes.UCSC.panTro3/BSgenome.Ptroglodytes.UCSC.panTro3_1.4.0.tar.gz"]

	version("1.4.0", md5="4677c75befd60742f3fc2a54c7f60666", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ptroglodytes.UCSC.panTro3_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

