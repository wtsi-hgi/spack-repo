# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmusculusUcscMm8(RPackage):
	"""Full genome sequences for Mus musculus (UCSC version mm8)

	Full genome sequences for Mus musculus (Mouse) as provided by UCSC (mm8, Feb. 2006) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Mmusculus.UCSC.mm8" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm8_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mmusculus.UCSC.mm8/BSgenome.Mmusculus.UCSC.mm8_1.4.0.tar.gz"]

	version("1.4.0", md5="f6aa91cdce2607f30a34f6dd0d678aff", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm8_1.4.0.tar.gz")
	version("1.4.0", md5="f6aa91cdce2607f30a34f6dd0d678aff", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm8_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

