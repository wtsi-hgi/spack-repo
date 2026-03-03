# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToposort(RPackage):
	"""Topological Sorting Algorithms

	Flexible and ergonomic topological sorting implementation for
    R. Supports a variety of input data encoding (lists of edges or
    adjacency matrices, graphs edge direction), stable sort variants as
    well as cycle detection with detailed diagnosis.
	"""
	
	homepage = "https://github.com/tzakharko/toposort"
	cran = "toposort" 

	version("1.0.0", md5="89b1a2a46e83827590a2ce407ed8ed51")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
