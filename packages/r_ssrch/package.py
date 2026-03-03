# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsrch(RPackage):
	"""a simple search engine

	Demonstrate tokenization and a search gadget for collections of CSV files.
	"""
	
	bioc = "ssrch" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ssrch_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ssrch/ssrch_1.18.0.tar.gz"]

	version("1.18.0", md5="095c153ce56b89d040c929a8c1af6840")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
