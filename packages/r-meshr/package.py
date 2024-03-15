# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeshr(RPackage):
	"""Tools for conducting enrichment analysis of MeSH

	A set of annotation maps describing the entire MeSH assembled using data from MeSH.
	"""
	
	bioc = "meshr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/meshr_2.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/meshr/meshr_2.8.0.tar.gz"]

	version("2.8.0", md5="7809b970dabdb3c42112e6b3aad5b75b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-meshdbi", type=("build", "run"))
	depends_on("r-category", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
