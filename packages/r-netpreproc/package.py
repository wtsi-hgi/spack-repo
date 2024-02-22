# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetpreproc(RPackage):
	"""Network Pre-Processing and Normalization

	Network Pre-Processing and normalization. Methods for normalizing graphs, including Chua normalization, Laplacian normalization, Binary magnification, min-max normalization and others. Methods to sparsify adjacency matrices. Methods for graph pre-processing and for filtering edges of the graph.
	"""
	
	cran = "NetPreProc" 

	version("1.2", md5="1403ec6044249b1240c7454f2f79cd85")

	depends_on("r-graph", type=("build", "run"))
