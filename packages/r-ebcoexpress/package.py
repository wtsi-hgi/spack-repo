# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbcoexpress(RPackage):
	"""EBcoexpress for Differential Co-Expression Analysis

	An Empirical Bayesian Approach to Differential Co-Expression Analysis at the Gene-Pair Level
	"""
	
	bioc = "EBcoexpress" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/EBcoexpress_1.46.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/EBcoexpress/EBcoexpress_1.46.0.tar.gz"]

	version("1.46.0", md5="66fa4257fbd0222064b30f6c15e74ab1")

	depends_on("r-ebarrays", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
