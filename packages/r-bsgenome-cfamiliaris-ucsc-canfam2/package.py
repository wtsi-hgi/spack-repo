# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCfamiliarisUcscCanfam2(RPackage):
	"""Full genome sequences for Canis lupus familiaris (UCSC version canFam2)

	Full genome sequences for Canis lupus familiaris (Dog) as provided by UCSC (canFam2, May 2005) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Cfamiliaris.UCSC.canFam2" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Cfamiliaris.UCSC.canFam2_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Cfamiliaris.UCSC.canFam2/BSgenome.Cfamiliaris.UCSC.canFam2_1.4.0.tar.gz"]

	version("1.4.0", sha256="151e18c084b397f271650703b8c9610e674bbee1a6b407b7ccc0db5035155714", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Cfamiliaris.UCSC.canFam2_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

