# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDendsort(RPackage):
	"""Modular Leaf Ordering Methods for Dendrogram Nodes

	An implementation of functions to optimize ordering of nodes in a dendrogram, without affecting the meaning of the dendrogram. A dendrogram can be sorted based on the average distance of subtrees, or based on the smallest distance value. These sorting methods improve readability and interpretability of tree structure, especially for tasks such as comparison of different distance measures or linkage types and identification of tight clusters and outliers. As a result, it also introduces more meaningful reordering for a coupled heatmap visualization. This method is described in "dendsort: modular leaf ordering methods for dendrogram representations in R", F1000Research 2014, 3: 177 <doi:10.12688/f1000research.4784.1>.
	"""
	
	homepage = "https://github.com/evanbiederstedt/dendsort"
	cran = "dendsort" 

	version("0.3.4", md5="aa431b861ec9dad6da1cfeb2b923edb9")

