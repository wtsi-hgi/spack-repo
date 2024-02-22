# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeTguttataUcscTaegut1(RPackage):
	"""Full genome sequences for Taeniopygia guttata (UCSC version taeGut1)

	Full genome sequences for Taeniopygia guttata (Zebra finch) as provided by UCSC (taeGut1, Jul. 2008) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Tguttata.UCSC.taeGut1" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Tguttata.UCSC.taeGut1_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Tguttata.UCSC.taeGut1/BSgenome.Tguttata.UCSC.taeGut1_1.4.0.tar.gz"]

	version("1.4.0", md5="9753d9568d2a866a627673a518a1dd8a", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Tguttata.UCSC.taeGut1_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation