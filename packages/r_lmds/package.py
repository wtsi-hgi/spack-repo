# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmds(RPackage):
	"""Landmark Multi-Dimensional Scaling

	
  A fast dimensionality reduction method scaleable to large numbers of samples.
  Landmark Multi-Dimensional Scaling (LMDS) is an extension of classical Torgerson MDS,
  but rather than calculating a complete distance matrix between all pairs of samples,
  only the distances between a set of landmarks and the samples are calculated.
	"""
	
	homepage = "http://github.com/dynverse/lmds"
	cran = "lmds" 

	version("0.1.0", md5="fb3298954e80b1700fea920760168f0c")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dynutils@1.0.3:", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
