# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeAthalianaTairTair9(RPackage):
	"""Full genome sequences for Arabidopsis thaliana (TAIR9)

	Full genome sequences for Arabidopsis thaliana as provided by TAIR (TAIR9 Genome Release) and stored in Biostrings objects. Note that TAIR10 is an "annotation release" based on the same genome assembly as TAIR9.
	"""
	
	bioc = "BSgenome.Athaliana.TAIR.TAIR9" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Athaliana.TAIR.TAIR9_1.3.1000.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Athaliana.TAIR.TAIR9/BSgenome.Athaliana.TAIR.TAIR9_1.3.1000.tar.gz"]

	version("1.3.1000", sha256="00d002e49a2da221f8a8bd64f8458bc63cef58546c7d1ea483cc160690d58558", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Athaliana.TAIR.TAIR9_1.3.1000.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

