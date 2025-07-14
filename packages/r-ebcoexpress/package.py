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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EBcoexpress_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EBcoexpress/EBcoexpress_1.46.0.tar.gz"]

    version("1.52.0", tag="RELEASE_3_21")
	version("1.46.0", sha256="19efec1bc5219b0658ea7aa78d96a3acb931176e86f27584891fbdcb470a1e35")

	depends_on("r-ebarrays", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
