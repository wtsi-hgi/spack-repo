# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeRnorvegicusUcscRn7(RPackage):
	"""Full genome sequences for Rattus norvegicus (UCSC genome rn7)

	Full genome sequences for Rattus norvegicus (Rat) as provided by UCSC (genome rn7) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Rnorvegicus.UCSC.rn7" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn7_1.4.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Rnorvegicus.UCSC.rn7/BSgenome.Rnorvegicus.UCSC.rn7_1.4.3.tar.gz"]

	version("1.4.3", sha256="be4547df2c9bce39d32b5d02a4f96831a37c62c2fbb20abe20d5e05c667ff52d", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Rnorvegicus.UCSC.rn7_1.4.3.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

