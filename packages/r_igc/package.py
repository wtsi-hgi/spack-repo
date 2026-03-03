# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgc(RPackage):
	"""An integrated analysis package of Gene expression and Copy number alteration

	This package is intended to identify differentially expressed genes driven by Copy Number Alterations from samples with both gene expression and CNA data.
	"""
	
	homepage = "http://github.com/ccwang002/iGC"
	bioc = "iGC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iGC_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iGC/iGC_1.32.0.tar.gz"]

	version("1.32.0", md5="14007fadd58eaea3e345ba53a279f783")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
