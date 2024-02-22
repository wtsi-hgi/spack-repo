# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSand(RPackage):
	"""Statistical Analysis of Network Data with R, 2nd Edition

	Data sets and code blocks for the book 'Statistical Analysis of 
  Network Data with R, 2nd Edition'.
	"""
	
	homepage = "https://github.com/kolaczyk/sand"
	cran = "sand" 

	version("2.0.0", md5="e2ba4b39eab063fb42912ef50dbcff71")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-igraphdata", type=("build", "run"))
