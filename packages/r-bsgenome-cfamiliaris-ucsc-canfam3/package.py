# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCfamiliarisUcscCanfam3(RPackage):
	"""Full genome sequences for Canis lupus familiaris (UCSC version canFam3)

	Full genome sequences for Canis lupus familiaris (Dog) as provided by UCSC (canFam3, Sep. 2011) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Cfamiliaris.UCSC.canFam3" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Cfamiliaris.UCSC.canFam3_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Cfamiliaris.UCSC.canFam3/BSgenome.Cfamiliaris.UCSC.canFam3_1.4.0.tar.gz"]

	version("1.4.0", sha256="99c55b6f7808822a3dae6679e60ecfb88a2b618159484bc35303c000bd4820c7", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Cfamiliaris.UCSC.canFam3_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

