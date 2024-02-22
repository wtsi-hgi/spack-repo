# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REconomiccomplexity(RPackage):
	"""Computational Methods for Economic Complexity

	A wrapper of different methods from Linear Algebra for the equations
  introduced in The Atlas of Economic Complexity and related literature. This
  package provides standard matrix and graph output that can be used seamlessly
  with other packages. See <doi:10.21105/joss.01866> for a summary
  of these methods and its evolution in literature.
	"""
	
	homepage = "https://pacha.dev/economiccomplexity/"
	cran = "economiccomplexity" 

	version("1.5.0", md5="5563b6070f9950a80a8851f9fce76409")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
