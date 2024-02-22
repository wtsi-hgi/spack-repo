# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordspace(RPackage):
	"""Distributional Semantic Models in R

	An interactive laboratory for research on distributional semantic models ('DSM',
             see <https://en.wikipedia.org/wiki/Distributional_semantics> for more information).
	"""
	
	homepage = "http://wordspace.r-forge.r-project.org/"
	cran = "wordspace" 

	version("0.2-8", md5="31576a5a40dd4044e8b99a45a3765a21")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix@1.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sparsesvd", type=("build", "run"))
	depends_on("r-iotools", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
