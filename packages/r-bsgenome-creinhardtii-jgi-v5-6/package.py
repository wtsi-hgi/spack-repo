# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCreinhardtiiJgiV56(RPackage):
	"""Full genome sequences for Chlamydomonas reinhardtii (v5.6)

	Full genome sequences for Chlamydomonas reinhardtii (v5.6) as provided by JGI and stored in Biostrings objects. The data in this package is public. See 'citation("BSgenome.Creinhardtii.JGI.v5.6")' for how to cite in publications.
	"""
	
	bioc = "BSgenome.Creinhardtii.JGI.v5.6" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Creinhardtii.JGI.v5.6_1.5.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Creinhardtii.JGI.v5.6/BSgenome.Creinhardtii.JGI.v5.6_1.5.0.tar.gz"]

	version("1.5.0", md5="2bd1be53d19249ac14ad7f39dc00af0e", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Creinhardtii.JGI.v5.6_1.5.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

