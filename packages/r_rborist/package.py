# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRborist(RPackage):
	"""Extensible, Parallelizable Implementation of the Random Forest
Algorithm

	Scalable implementation of classification and regression forests, as described by Breiman (2001), <DOI:10.1023/A:1010933404324>.
	"""
	
	homepage = "https://github.com/suiji/Rborist.CRAN"
	cran = "Rborist" 

	version("0.3-7", md5="38b7632d56300976315dbac4ad93b415")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
