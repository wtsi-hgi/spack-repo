# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCjacchusUcscCaljac4(RPackage):
	"""Full genome sequences for Callithrix jacchus (UCSC version calJac4)

	Full genome sequences for Callithrix jacchus (Marmoset) as provided by UCSC (calJac4, May 2020) and wrapped in a BSgenome object.
	"""
	
	bioc = "BSgenome.Cjacchus.UCSC.calJac4" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Cjacchus.UCSC.calJac4_1.5.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Cjacchus.UCSC.calJac4/BSgenome.Cjacchus.UCSC.calJac4_1.5.0.tar.gz"]

	version("1.5.0", sha256="2edf92dfcd98a5427ca5ad482e84dc37819f43564a0c603286c554969566d941", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Cjacchus.UCSC.calJac4_1.5.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

