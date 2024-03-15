# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIterclust(RPackage):
	"""Iterative Clustering

	A framework for performing clustering analysis iteratively.
	"""
	
	homepage = "https://github.com/hd2326/iterClust"
	bioc = "iterClust" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iterClust_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iterClust/iterClust_1.24.0.tar.gz"]

	version("1.24.0", md5="af72d13d4200d5883ae63a99f0a49a69")

	depends_on("r@3.4.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
