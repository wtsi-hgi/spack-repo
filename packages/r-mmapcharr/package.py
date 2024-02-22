# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmapcharr(RPackage):
	"""Memory-Map Character Files

	Uses memory-mapping to enable the random access of elements of
  a text file of characters separated by characters as if it were a simple
  R(cpp) matrix.
	"""
	
	homepage = "https://github.com/privefl/mmapcharr"
	cran = "mmapcharr" 

	version("0.3.0", md5="4b84d1fe1f6646476d87d0e730b355c3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rmio", type=("build", "run"))
