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

	version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="b911f1b49760de5c1a64b52cdc724429cb70aeb6408b45a1dde4b30a370b6b3f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
